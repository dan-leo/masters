from process.globals import *

to_bin = lambda x, n: format(x, 'b').zfill(n)

def capture(limit, file='dump'):
    filename = './logs/' + file
    print('CAPTURE START')
    begin = True
    with open(filename, 'a+') as f:
        pass
    with open(filename, 'r') as f:
        if 'index,' in f.readline():
            begin = False
    sendTIM('s')
    index = 0
    buf = []
    try:
        while True:
            with open(filename, 'a+') as f:
                data = receiveTIM()
                if data:
                    # print(data)
                    sendTIM('e')
                    nue = nuestats()

                    # print header
                    if begin:
                        if not len(nue):
                            buf.append(data)
                            continue
                        msg = 'index,'
                        print(green + 'index,')
                        for key in data:
                            msg += key + ','
                            print(key, end=',')
                        for key in nue:
                            msg += key + ','
                            print(key, end=',')
                        print()
                        f.write(msg + '\n')
                        begin = False

                    # in case nuestat not working initially
                    if len(buf):
                        for b in buf:
                            msg = yellow + str(index) + ',' + red + dictToCSV(b)
                            print(msg)
                            msg = str(index) + ',' + dictToCSV(b)
                            f.write(msg + '\n')
                        buf = []
                    msg = yellow + str(index) + ',' + red + dictToCSV(data) + blue + dictToCSV(nue)
                    print(msg)
                    msg = str(index) + ',' + dictToCSV(data) + dictToCSV(nue)
                    f.write(msg + '\n')
                    sendTIM('s')
                    index += 1
                    if index == limit:
                        break
    except KeyboardInterrupt:
        pass
    finally:
        print('CAPTURE END')
        sendTIM('s')

def dictToCSV(dictionary):
    csv = ""
    for key in dictionary:
        csv += str(dictionary[key]) + ','
    # print(red + csv)
    return csv

def nuestats():
    data = expect('at+nuestats="ALL"', 'OK', output=False)[:-1]
#     data = []
#     for d in expect('at+nuestats="RADIO"', 'OK', output=False)[:-1]:
#         data.append(d)
#     for d in expect('at+nuestats="BLER"', 'OK', output=False)[:-1]:
#         data.append(d)
#     data.append(expect('at+nuestats="CELL"', 'OK', output=False)[:-1])
    # print(blue + str(data))
    dr = {}
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
    return dr

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