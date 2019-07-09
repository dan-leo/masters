from process.globals import *

to_bin = lambda x, n: format(x, 'b').zfill(n)

def capture(limit):
    print('CAPTURE START')
    begin = True
    sendTIM('s')
    index = 0
    try:
        while True:
            data = receiveTIM()
            if data:
                # print(data)
                sendTIM('e')
                nue = nuestats()
                if begin:
                    print(green + 'index,',end="")
                    for key in data:
                        print(key, end=",")
                    for key in nue:
                        print(key, end=",")
                    print()
                    begin = False
                print(yellow + str(index) + ',' + red + dictToCSV(data) + blue + dictToCSV(nue))
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
    # print(blue + data)
    dr = {}
    for i in data:
        j = i.split(',')
        if j[0] == 'NUESTATS: "APPSMEM"':
            dr[j[1].split(':')[0][1:-1]] = j[1].split(':')[1]
        elif j[0] == 'NUESTATS: "CELL"':
            dr['primary_cell'] = j[3]
            dr['rsrp'] = j[4]
            dr['rsrq'] = j[5]
            dr['rssi'] = j[6]
            dr['snr'] = j[7]
        elif 'NUESTATS' in j[0]:
            dr[j[1][1:-1]] = j[2]
    return dr

def edrxQuery():
    expect('AT+NPTWEDRXS?', 'NPTWEDRXS', output=False)
    expect('at+cpsms?', 'CPSMS', output=False)

def setEDRX(ptw = 0, edrx = 9, active = 0, activeMul = 5, ptau = 3, ptauMul = 10, output=True):
    data = expect('AT+NPTWEDRXS=2,5,"' + str(to_bin(ptw, 4)) + '","' + str(to_bin(edrx, 4)) + '"', reply='', t=3, output=output) # +CSCON: 0
    receiveAT(t=1, output=output)
    data = expect('at+cpsms=1,,,"' + str(to_bin(ptau, 3)) + str(to_bin(ptauMul, 5)) + '","' + str(to_bin(active, 3)) + str(to_bin(activeMul, 5)) + '"', reply='', t=3, output=output) # +NPSMR:
    receiveAT(t=1, output=output)
    # receiveAT(2, expect='+NPTWEDRXP')
    edrxQuery()
#     receiveTIM()