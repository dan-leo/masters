import serial
import colorama
import sys
import time
import pytest
import numpy as np
import math

from process import timing_bits as p

colorama.init()
serAT = serial.Serial('COM108', 9600, timeout=1)
serTIM = serial.Serial('COM15', 115200, timeout=1)
to_bin = lambda x, n: format(x, 'b').zfill(n)

black   =  '\033[1;30m'
red     =  '\033[1;31m'
green   =  '\033[1;32m'
yellow  =  '\033[1;33m'
blue    =  '\033[1;34m'
magenta =  '\033[1;35m'
cyan    =  '\033[1;36m'
white   =  '\033[1;37m'

nw_edrx = ["0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111","0010","0011","0010","0101","0010","1001","1010","1011","1100","1101","1110","1111"]
nw_ptw  = ["0000","0000","0000","0000","0000","0000","0000","0000","0000","0000","0000","0000","0001","0001","0001","0001","0001","0001","0001","0001","0001","0001","0001","0001","0010","0010","0010","0010","0010","0010","0010","0010","0010","0010","0010","0010","0011","0011","0011","0011","0011","0011","0011","0011","0011","0011","0011","0011","0100","0100","0100","0100","0100","0100","0100","0100","0100","0100","0100","0100","0101","0101","0101","0101","0101","0101","0101","0101","0101","0101","0101","0101","0110","0110","0110","0110","0110","0110","0110","0110","0110","0110","0110","0110","0111","0111","0111","0111","0111","0111","0111","0111","0111","0111","0111","0111","1000","1000","1000","1000","1000","1000","1000","1000","1000","1000","1000","1000","1001","1001","1001","1001","1001","1001","1001","1001","1001","1001","1001","1001"]

print (yellow, 'Welcome to the', green, 'AT command', yellow, 'tester by Daniel Robinson.')

def sendTIM(cmd):
    print(yellow + cmd)
    serTIM.write(bytes(cmd + '\r', 'utf-8'))

def receiveTIM():
    c = 0
    a = []
    b = []
    g = 0
    while True:
        d = serTIM.readline().decode('utf-8')
        if not len(d):
            c += 1
        else:
            d = d.strip()
            a.append(d)
            b.append(int(d.split(',')[0]))
            print(white + d, blue + str(b))
            g = guess_seq_len(b)
            if g != 0:
                print(magenta + str(g))
                break

def test_rec():
    receiveTIM()
    
def sendAT(cmd, t=0, expect='OK'):
    print(yellow + cmd)
    serAT.write(bytes(cmd + '\r', 'utf-8'))
    return receiveAT(t, expect)

def receiveAT(t=0, expect='OK'):
    c = 0
    data = []
    while True:
        d = serAT.readline().decode('utf-8')
        if not len(d):
            c += 1
        d = d.strip()
        if len(d) > 0:
            print(cyan + d)
            out = p.converter(d)
            if out:
                print(magenta + out)
            data.append(d)
        if t > 0:
            if c == t:
                data.append('timeout')
                return data
        if expect in d or 'ERROR' in d:
            return data

def OK(cmd, t=0):
    assert 'OK' in sendAT(cmd, t)

def expect(cmd, reply, t=1):
    data = sendAT(cmd, t, reply)
    assert True in [reply in i for i in data]
    return data
    
@pytest.mark.setup
def test_connect():
    assert serAT.is_open == True

@pytest.mark.setup
def test_AT():
    OK('AT')

@pytest.mark.setup
def test_NCONFIG():
    OK('AT+NCONFIG="AUTOCONNECT","FALSE"')
    OK('AT+NCONFIG="CR_0859_SI_AVOID","TRUE"')
    OK('AT+NCONFIG="CR_0354_0338_SCRAMBLING","TRUE"')

@pytest.mark.setup
def test_URC():
    OK('AT+CMEE=1')
    OK('AT+CSCON=1')
    OK('AT+CEREG=5')
    OK('AT+NPSMR=1')

@pytest.mark.setup
def test_CFUN():
    OK('AT+CFUN=0', 3)
    expect('at+cfun?', '+CFUN: 0', 1)
    expect('AT+CFUN=1', '+CEREG: 0', 2)
    receiveAT()

@pytest.mark.setup
def test_COPS():
    expect('AT+COPS=0', '+CEREG: 1', 10)

@pytest.mark.setup
def test_CEREG():
    expect('AT+CEREG?', '+CEREG: 5,1')

@pytest.mark.setup
def test_ping():
    expect('at+nping="8.8.8.8"', '+NPING: "8.8.8.8"', 10)

@pytest.mark.setup
def test_release():
    expect('at+cops=2', '+NPSMR: 1', 10)
    expect('at+cops=0', '+CEREG: 1', 10)
    OK('AT+NSOCR="DGRAM",17,14000,1')
    expect('AT+NSOSTF=0,"1.1.1.1",7,0x200,1,"FF"', '+CSCON: 0', 10)
    OK('at+nsocl=0')

@pytest.mark.edrx
def test_eDRX():
    for edrx in range(10):
        for ptw in range(16):
            data = expect('AT+NPTWEDRXS=2,5,"' + str(to_bin(ptw, 4)) + '","' + str(to_bin(edrx, 4)) + '"', '+CSCON: 0', 10)
            receiveAT(2, expect='+NPTWEDRXP')
            expect('AT+NPTWEDRXS?', 'NPTWEDRXS')

@pytest.mark.edrx_nw
def test_NWeDRX():
    for ptw, edrx in zip(nw_ptw, nw_edrx):
        data = expect('AT+NPTWEDRXS=2,5,"' + ptw + '","' + edrx + '"', '+CSCON: 0', 10)
        # receiveAT(2, expect='+NPTWEDRXP')
        # expect('AT+NPTWEDRXS?', 'NPTWEDRXS')


@pytest.mark.file_edrx
def test_file_eDRX():
    # fileEDRX = open('eDRX ' + time.strftime("%Y%m%d-%H%M%S") + '.log', "w+")
    f = open("nw_edrx.log", "r")
    fx = open('nw_edrx.csv', "w+")
    lines = f.readlines()
    for l in lines:
        print(p.csv(l))
        fx.write(p.csv(l) + '\n')

def guess_seq_len(seq):
    # find number of sequences in similar arrays
    # limited to a maximum difference
    maxDiff = 100
    guess = 0
    max_len = math.ceil(len(seq) / 2)
    for s in range(len(seq)):
        for x in range(1, max_len - s + 1):
            a = abs(np.array(seq[s:s+x]) - np.array(seq[s+x:s+2*x]))
            if len(a) and not False in (a < np.array([maxDiff] * len(a))):
                print(x, s, a, seq[s:s+x], "==", seq[s+x:s+2*x])
                return x
    return guess

def test_findRepetition():
    f = open("logs/pulses0x1331NWeDRX81.92PTW5.21.log", "r")
    lines = f.readlines()
    a = []
    for l in lines:
        a.append(int(l.split(',')[0]))
    print(guess_seq_len(a))

def test_close():
    serAT.close()
    serTIM.close()
    assert serAT.is_open == False
    assert serTIM.is_open == False

if __name__ == '__main__':
    test_close()