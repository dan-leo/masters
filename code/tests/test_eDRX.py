from __future__ import print_function
from process.globals import *

colorama.init()
to_bin = lambda x, n: format(x, 'b').zfill(n)

nw_edrx = ["0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111"]
nw_ptw  = ["0000","0000","0000","0000","0000","0000","0000","0000","0000","0000","0000","0000","0001","0001","0001","0001","0001","0001","0001","0001","0001","0001","0001","0001","0010","0010","0010","0010","0010","0010","0010","0010","0010","0010","0010","0010","0011","0011","0011","0011","0011","0011","0011","0011","0011","0011","0011","0011","0100","0100","0100","0100","0100","0100","0100","0100","0100","0100","0100","0100","0101","0101","0101","0101","0101","0101","0101","0101","0101","0101","0101","0101","0110","0110","0110","0110","0110","0110","0110","0110","0110","0110","0110","0110","0111","0111","0111","0111","0111","0111","0111","0111","0111","0111","0111","0111","1000","1000","1000","1000","1000","1000","1000","1000","1000","1000","1000","1000","1001","1001","1001","1001","1001","1001","1001","1001","1001","1001","1001","1001"]

# print (yellow, 'Welcome to the', green, 'AT command', yellow, 'tester by Daniel Robinson.')

def setup_module(module):
    serialOpen()
 
def teardown_module(module):
    serialClose()

def test_serial():
    import serial.tools.list_ports
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))
        print(hwid.split('=')[1].split()[0])

def dictToCSV(dictionary):
    csv = ""
    for key in dictionary:
        csv += str(dictionary[key]) + ','
    # print(red + csv)
    return csv

def test_capture():
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
                
    except KeyboardInterrupt:
        pass
    finally:
        print('CAPTURE END')

def nuestats():
    data = []
    for d in expect('at+nuestats="RADIO"', 'OK', output=False)[:-1]:
        data.append(d)
    for d in expect('at+nuestats="BLER"', 'OK', output=False)[:-1]:
        data.append(d)
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

def test_nuestats():
    print(yellow + nuestats())

# @pytest.mark.skip()
# @pytest.mark.edrx
def test_edrx1():
    for edrx in range(10):
        for ptw in range(16):
            # primeTIM()
            data = expect('AT+NPTWEDRXS=2,5,"' + str(to_bin(ptw, 4)) + '","' + str(to_bin(edrx, 4)) + '"', '+CSCON: 0', 10)
            # receiveAT(2, expect='+NPTWEDRXP')
            expect('AT+NPTWEDRXS?', 'NPTWEDRXS')
            receiveTIM()

def test_view():
        tPeriodicTau = [600, 3600, 36000, 2, 30, 60, 1152000, 0]
        tActive = [2, 60, 360, 0]
        tEDRX = [10.24, 20.48, 40.96, 81.92, 163.84, 327.68, 655.36, 1310.72, 1966.08, 2621.44]
        tPTW = [2.56,5.12,7.68,10.24,12.8,15.36,17.92,20.48,23.04,25.6,28.16,30.72,33.28,35.84,38.4,40.96]

# 2340,33501,35841,116366.94,108
# 9521,29339,38860,62170.99,127

def setEDRX(ptw = 0, edrx = 9, active = 0, activeMul = 5, ptau = 3, ptauMul = 10):
    data = expect('AT+NPTWEDRXS=2,5,"' + str(to_bin(ptw, 4)) + '","' + str(to_bin(edrx, 4)) + '"', '', 3) # +CSCON: 0
    receiveAT(1)
    data = expect('at+cpsms=1,,,"' + str(to_bin(ptau, 3)) + str(to_bin(ptauMul, 5)) + '","' + str(to_bin(active, 3)) + str(to_bin(activeMul, 5)) + '"', '', 3) # +NPSMR:
    receiveAT(1)
    # receiveAT(2, expect='+NPTWEDRXP')
    test_edrxQuery()
#     receiveTIM()

def test_edrxSet():
#     setEDRX(0, 9, 0, 5, 3, 10) # off
#     setEDRX(1, 4, 0, 5, 3, 10) # 20 sec delay. 2 drx. 30 sec ptau
#     setEDRX(0, 0, 0, 5, 3, 10) # 2.56 continuous
#     setEDRX(1, 0, 0, 10, 3, 15) # 2.56 cont, 30 sec ptau
#     setEDRX(0, 0, 0, 0, 3, 2) # 5.5 sec ptau
#     setEDRX(0, 1, 0, 1, 0, 1) # 12 2.56 DRX for 30 sec. silence after
#     setEDRX(0, 2, 0, 15, 3, 20) # one DRX at 20 sec. 30e, 30a, 40p
    setEDRX(0, 1, 0, 15, 3, 20)

# AT+NSOCR="DGRAM",17,14000
def test_echo():
    # expect('at+cops=2', '+NPSMR: 1', 10)
    # expect('at+cops=0', '+CEREG: 1', 10)
#     OK('at+nsocl=0')
    OK('AT+NSOCR="DGRAM",17,14000')
#     expect('AT+NSOST=0,"195.34.89.241",7,5,"48656c6c6F"', '+CSCON: 1', 10)
    expect('AT+NSOSTF=0,"195.34.89.241",7,0x200,1,"FF"', '+CSCON: 0', 10)
    receiveAT(2)
    OK('AT+NSORF=0,5', 3)
    OK('at+nsocl=0')
    

def test_ptauConfigs():
    edrx = 0
    ptw = 0
    active = 0
    activeMul = 5
    ptau = 3
    ptauMul = 8
    data = expect('AT+NPTWEDRXS=2,5,"' + str(to_bin(ptw, 4)) + '","' + str(to_bin(edrx, 4)) + '"', '', 3)
    receiveAT(1)
    for a in range(32):
        for aVal in range(8):
            data = expect('at+cpsms=1,,,"' + str(to_bin(ptau, 3)) + str(to_bin(ptauMul, 5)) + '","' + str(to_bin(a, 3)) + str(to_bin(aVal, 5)) + '"', '', 3) # +NPSMR:
        #     print(data)
            data = receiveAT(1)
        #     print(data)
            if 'ERROR' in data[0]:
                expect('at+cpsms?', '')

def test_edrxQuery():
    expect('AT+NPTWEDRXS?', 'NPTWEDRXS', output=False)
    expect('at+cpsms?', 'CPSMS', output=False)

# @pytest.mark.skip()
# @pytest.mark.edrx_nw
def test_edrxNW():
    for ptw, edrx in zip(nw_ptw, nw_edrx):
        data = expect('AT+NPTWEDRXS=2,5,"' + ptw + '","' + edrx + '"', '+CSCON: 0', 10)
        receiveTIM()
        # receiveAT(2, expect='+NPTWEDRXP')
        # expect('AT+NPTWEDRXS?', 'NPTWEDRXS')

# @pytest.mark.skip()
# @pytest.mark.file_edrx
def test_edrxFile():
    # fileEDRX = open('eDRX ' + time.strftime("%Y%m%d-%H%M%S") + '.log', "w+")
    f = open("./logs/nw_edrx.log", "r")
    fx = open('./logs/nw_edrx.csv', "w+")
    lines = f.readlines()
    for l in lines:
        print(csv(l))
        fx.write(csv(l) + '\n')

def test_findRepetition():
    f = open("logs/pulses0x1331NWeDRX81.92PTW5.21.log", "r")
    lines = f.readlines()
    a = []
    for l in lines:
        a.append(int(l.split(',')[0]))
    print(guess_seq_len(a))

# def test_close():
#     serAT.close()
#     serTIM.close()
#     assert serAT.is_open == False
#     assert serTIM.is_open == False
#     assert serGPS.is_open == False

# if __name__ == '__main__':
#     test_close()