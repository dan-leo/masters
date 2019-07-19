from process.globals import *
import serial.tools.list_ports

black   =  '\033[1;30m'
red     =  '\033[1;31m'
green   =  '\033[1;32m'
yellow  =  '\033[1;33m'
blue    =  '\033[1;34m'
magenta =  '\033[1;35m'
cyan    =  '\033[1;36m'
white   =  '\033[1;37m'

AT_PORT = 'COM106'
uC_PORT = 'COM121'
GPS_PORT = 'COM83'

serAT = serial.Serial()
serTIM = serial.Serial()
serGPS = serial.Serial()

def serialOpen():
    global serAT, serTIM, serGPS, AT_PORT, uC_PORT
    ATcount = 0
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        # print("{}: {} [{}]".format(port, desc, hwid))
        vid_pid = hwid.split('=')[1].split()[0]
        # print(vid_pid)
        if vid_pid == '2341:8036':
            uC_PORT = port
        if vid_pid == '0403:6010' and not ATcount:
            AT_PORT = port
            ATcount += 1
            pytest.vendor = 'ublox'
        if vid_pid == '04E2:1414' and ATcount < 1:
            AT_PORT = port
            ATcount += 1
            pytest.vendor = 'quectel'
        if vid_pid == '0403:6001':
            AT_PORT = port
            pytest.vendor = 'simcom'
    try:
        serAT = serial.Serial(AT_PORT, 115200, timeout=0.1)
        serTIM = serial.Serial(uC_PORT, 115200, timeout=1)
        serGPS = serial.Serial(GPS_PORT, 9600, timeout=1)
    except serial.serialutil.SerialException as e:
        pass
        # print(e)

def serialClose():
    global serAT, serTIM, serGPS
    serAT.close()
    serTIM.close()
    serGPS.close()


def sendTIM(cmd):
    # print(yellow + cmd)
    pass
    # serTIM.write(bytes(cmd + '\r', 'utf-8'))

def primeTIM():
    serTIM.write('r'.encode())

def receiveTIM():
    data = {}
    d = serTIM.readline().decode('utf-8')
    # d = '2300,260,2560,10.0,100,'
    if len(d):
        try:
            d = d.strip()
            data['idleTime'] = int(d.split(',')[0])
            data['txTime'] = int(d.split(',')[1])
            data['totalTime'] = int(d.split(',')[2])
            data['energy'] = float(d.split(',')[3])
            data['maxCurrent'] = float(d.split(',')[4])
        except (ValueError, IndexError) as e:
            print(d)
            raise e
    return data

    # g = 0
    # now = time.time()
    # while True and (time.time() - now < 600.0):
    while True:
            # print(white + d, blue + str(energy))
            break
            # if energy[-1] > 25.0:

            # g = guess_seq_len(b)
            # if g != 0:
            #     print(magenta + str(g))
            #     break
    
def sendAT(cmd, t=0, expect=['OK'], output=True):
    if output and pytest.output:
        print(yellow + cmd)
    serAT.write(bytes(cmd + '\r', 'utf-8'))
    return receiveAT(t, expect, output)

def streamAT():
    while True:
        d = serAT.readline().decode('utf-8')
        d = d.strip()
        if len(d):
            if pytest.nuelock:
                pytest.nuestream.append(d)
            else:
                pytest.stream.append(d)
            if pytest.output:
                print(cyan + d)
            out = converter(d)
            if out:
                print(magenta + out)

def receiveAT(t=0, expect=['OK'], output=True):
    if str(type(expect)) == "<class 'str'>":
        expect = [expect]
    c = 0
    data = []
    exp = expect[:]
    exp.append('ERROR')
    exp.append('FAILED')
    # while True:
    #     d = serAT.readline().decode('utf-8')
    #     if not len(d):
    #         c += 0.1
    #     if t > 0 and c == t:
    #         data.append('timeout')
    #         return data
    #     if len(d):
    #         data.append(d)

    datastream = []
    length = 0
    br = False
    while c < t:
        # print('br', br)
        if br:
            break
        if pytest.nuelock:
            datastream = pytest.nuestream[:]
            print(datastream, 'pytest.nuestream[:]', len(pytest.nuestream))
        else:
            datastream = pytest.stream[:]
        print('datastream', datastream)
        if len(datastream) != length:
            length = len(datastream)
            for e in exp:
                print('e in datastream', e in datastream, e)
                if e in datastream:
                    break
        br = True
        # else:
        #     # print('len(datastream) != length', len(datastream) != length, len(datastream), length)
        #     time.sleep(0.1)
        #     c += 0.1
    # else:
        # print("datastream.append('timeout')", c)
        # datastream.append('timeout')
    ret = datastream[:]
    if pytest.nuelock:
        pytest.nuestream = []
    else:
        pytest.stream = []
    return ret


    # while True:
    #     d = serAT.readline().decode('utf-8')
    #     if not len(d):
    #         c += 1
    #     d = d.strip()
    #     if len(d) > 0:
    #         if output:
    #             print(cyan + d)
    #         out = converter(d)
    #         if out:
    #             print(magenta + out)
    #         data.append(d)
    #     if t > 0:
    #         if c == t:
    #             data.append('timeout')
    #             return data
    #     for e in exp:
    #         if e in d:
    #             return data

def OK(cmd, t=0):
    reply = sendAT(cmd, t)
    print('reply:', reply)
    assert 'OK' in reply

def expect(cmd, reply, t=1, output=True):
    replies = reply
    if str(type(reply)) == "<class 'str'>":
        replies = [reply]
    data = sendAT(cmd, t, replies, output)
    if not len(replies[0]):
        return data
    check = False
    for r in replies:
        if len(r):
            if True in [r in i for i in data]:
                check = True
                break
    if not check:
        print(magenta + str(replies), data, cmd, pytest.stream, len(pytest.nuestream), len(data))
    assert check
    return data