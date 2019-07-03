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

# TODO: autodetect comm port
AT_PORT = 'COM106'
uC_PORT = 'COM121'
GPS_PORT = 'COM83'

serAT = serial.Serial()
serTIM = serial.Serial()
serGPS = serial.Serial()

def serialOpen():
    global serAT, serTIM, serGPS
    ATcount = 0
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        # print("{}: {} [{}]".format(port, desc, hwid))
        vid_pid = hwid.split('=')[1].split()[0]
        if vid_pid == '2341:8036':
            uC_PORT = port
        if vid_pid == '0403:6010' and not ATcount:
            AT_PORT = port
            ATcount += 1
    try:
        serAT = serial.Serial(AT_PORT, 9600, timeout=1)
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
    print(yellow + cmd)
    serTIM.write(bytes(cmd + '\r', 'utf-8'))

def primeTIM():
    serTIM.write('r'.encode())

def receiveTIM():
    data = {}
    d = serTIM.readline().decode('utf-8')
    if len(d):
        d = d.strip()
        data['idleTime'] = int(d.split(',')[0])
        data['txTime'] = int(d.split(',')[1])
        data['totalTime'] = int(d.split(',')[2])
        data['energy'] = float(d.split(',')[3])
        data['maxCurrent'] = float(d.split(',')[4])
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
    
def sendAT(cmd, t=0, expect='OK', output=True):
    if output:
        print(yellow + cmd)
    serAT.write(bytes(cmd + '\r', 'utf-8'))
    return receiveAT(t, expect, output)

def receiveAT(t=0, expect='OK', output=True):
    c = 0
    data = []
    while True:
        d = serAT.readline().decode('utf-8')
        if not len(d):
            c += 1
        d = d.strip()
        if len(d) > 0:
            if output:
                print(cyan + d)
            out = converter(d)
            if out:
                print(magenta + out)
            data.append(d)
        if t > 0:
            if c == t:
                data.append('timeout')
                return data
        if expect in d or 'ERROR' in d or 'FAILED' in d:
            return data

def OK(cmd, t=0):
    assert 'OK' in sendAT(cmd, t)

def expect(cmd, reply, t=1, output=True):
    data = sendAT(cmd, t, reply, output)
    if len(reply):
        assert True in [reply in i for i in data]
    return data