from test_ import *

nw_edrx = ["0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111"]
nw_ptw  = ["0000","0000","0000","0000","0000","0000","0000","0000","0000","0000","0000","0000","0001","0001","0001","0001","0001","0001","0001","0001","0001","0001","0001","0001","0010","0010","0010","0010","0010","0010","0010","0010","0010","0010","0010","0010","0011","0011","0011","0011","0011","0011","0011","0011","0011","0011","0011","0011","0100","0100","0100","0100","0100","0100","0100","0100","0100","0100","0100","0100","0101","0101","0101","0101","0101","0101","0101","0101","0101","0101","0101","0101","0110","0110","0110","0110","0110","0110","0110","0110","0110","0110","0110","0110","0111","0111","0111","0111","0111","0111","0111","0111","0111","0111","0111","0111","1000","1000","1000","1000","1000","1000","1000","1000","1000","1000","1000","1000","1001","1001","1001","1001","1001","1001","1001","1001","1001","1001","1001","1001"]

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

# @pytest.mark.skip()
# @pytest.mark.edrx_nw
def test_edrxNW():
    for ptw, edrx in zip(nw_ptw, nw_edrx):
        data = expect('AT+NPTWEDRXS=2,5,"' + ptw + '","' + edrx + '"', '+CSCON: 0', 10)
        receiveTIM()
        # receiveAT(2, expect='+NPTWEDRXP')
        # expect('AT+NPTWEDRXS?', 'NPTWEDRXS')

def test_PTAUconfigs():
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