from process.globals import *

to_bin = lambda x, n: format(x, 'b').zfill(n)

thread = False

# def tcap(limit=1000, log=''):
#     thread = threading.Thread(target=capture, args=[limit, log])
#     thread.daemon=True
#     thread.start()

def fwrite(path, data):
    pass

def checkFile(file):
    path = r'./logs/' + pytest.manufacturer + '_' + pytest.loc + pytest.vendor + '/' + pytest.test + pytest.subtest + pytest.descr
    if len(file):
        path += '_' + file
    print(yellow + path + white)
    try:
        with open(path, 'a+') as f:
            pass
    except (FileNotFoundError, PermissionError):
        slash = path[::-1].index('/')
        directory = path[:-slash]
        # file = path[-slash:]
        # filename = directory + file
        os.makedirs(directory)
        with open(path, 'a+') as f:
            pass
    with open(path, 'r') as f:
        return path, 'index,' in f.readline()

def capture(limit=1000, timeout=0, file=''):
    print('CAPTURE START')
    # sendTIM('s')
    index = 0
    buf = []
    tStart = time.time()
    try:
        while True:
            if time.time() - tStart > timeout and timeout:
                break

            # try:
            data = receiveTIM()
            # except:
            #     data = ''
            if data:
                flushTIM()
                # print(data)
                # sendTIM('e')
                nue = nuestats()
                # print(nue)

                # if no header or file does not exist
                path, header_exists = checkFile(file)

                with open(path, 'a+') as f:

                    if not header_exists:
                        if not len(nue):
                            buf.append(data)
                            continue
                        msg = 'index,'
                        print(cyan + 'index,')
                        for key in data:
                            msg += key + ','
                            print(key, end=',')
                        for key in nue:
                            msg += key + ','
                            print(key, end=',')
                        print()
                        f.write(msg + '\n')

                    # in case nuestat not working initially
                    if len(buf):
                        for b in buf:
                            msg = green + str(index) + ',' + red + dictToCSV(b)
                            print(msg)
                            msg = str(index) + ',' + dictToCSV(b)
                            f.write(msg + '\n')
                        buf = []

                    msg = green + str(index) + ',' + red + dictToCSV(data) + blue + dictToCSV(nue)
                    print(msg)
                    msg = str(index) + ',' + dictToCSV(data) + dictToCSV(nue)
                    f.write(msg + '\n')
                    # sendTIM('s')
                    index += 1
                    if index == limit and limit:
                        break
    except KeyboardInterrupt:
        pass
    finally:
        print('CAPTURE END')
        # sendTIM('s')

def dictToCSV(dictionary):
    csv = ""
    for key in dictionary:
        csv += str(dictionary[key]) + ','
    # print(red + csv)
    return csv

def nuestats():
#     data = []
#     for d in expect('at+nuestats="RADIO"', 'OK', output=False)[:-1]:
#         data.append(d)
#     for d in expect('at+nuestats="BLER"', 'OK', output=False)[:-1]:
#         data.append(d)
#     data.append(expect('at+nuestats="CELL"', 'OK', output=False)[:-1])
    # print(blue + str(data))
    for i in range(10):
        try:
            # print('for i in range(10):', i)
            data = expect('at+nuestats="ALL"', 'OK', output=False)[:-1]
        except AssertionError:
            continue
        dr = {}
        try:
            for i in data:
                j = i.split(',')
                # print(j)
                if j[0] == 'NUESTATS: "APPSMEM"' or j[0] == 'NUESTATS:APPSMEM':
                    dr[j[1].split(':')[0][1:-1]] = j[1].split(':')[1]
                elif j[0] == 'NUESTATS: "CELL"' or j[0] == 'NUESTATS:CELL':
                    dr['primary_cell'] = j[3]
                    dr['rsrp'] = j[4]
                    dr['rsrq'] = j[5]
                    dr['rssi'] = j[6]
                    dr['snr'] = j[7]
                elif 'NUESTATS:RADIO' in j[0]:
                    s = j[1].split(':')
                    dr[s[0]] = s[1]
                elif 'NUESTATS' in j[0]:
                    dr[j[1][1:-1]] = j[2]
        except IndexError as e:
            print(e)
            continue
        if len(dr):
            return dr
    else:
        return {}

def edrxQuery():
    expect('AT+NPTWEDRXS?', 'NPTWEDRXS', output=True)
    expect('at+cpsms?', 'CPSMS', output=True)

def setEDRX(ptw = 0, edrx = 9, active = 0, activeMul = 5, ptau = 3, ptauMul = 10, output=True):
    if pytest.vendor == 'ublox':
        data = expect('AT+NPTWEDRXS=2,5,"' + str(to_bin(ptw, 4)) + '","' + str(to_bin(edrx, 4)) + '"', reply='', t=3, output=output) # +CSCON: 0
        receiveAT(t=1, output=output)
        data = expect('at+cpsms=1,,,"' + str(to_bin(ptau, 3)) + str(to_bin(ptauMul, 5)) + '","' + str(to_bin(active, 3)) + str(to_bin(activeMul, 5)) + '"', reply='', t=3, output=output) # +NPSMR:
        receiveAT(t=1, output=output)
        # receiveAT(2, expect='+NPTWEDRXP')
        edrxQuery()
    #     receiveTIM()
    if pytest.vendor == 'quectel':
        pass
    if pytest.vendor == 'simcom':
        data = expect('AT*MEDRXCFG=1,5,"' + str(to_bin(edrx, 4)) + '","' + str(to_bin(ptw, 4)) + '"', reply='', t=3, output=output) # +CSCON: 0
        receiveAT(t=1, output=output)
        data = expect('AT+CPSMS=1,,,"' + str(to_bin(ptau, 3)) + str(to_bin(ptauMul, 5)) + '","' + str(to_bin(active, 3)) + str(to_bin(activeMul, 5)) + '"', reply='', t=3, output=output) # +NPSMR:
        receiveAT(t=1, output=output)