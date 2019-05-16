import unittest
import serial
import colorama
import sys
import time
import pytest

from process import timing_bits as p

colorama.init()
ser = serial.Serial('COM108', 9600, timeout=1)
to_bin = lambda x, n: format(x, 'b').zfill(n)

black   =  '\033[1;30m'
red     =  '\033[1;31m'
green   =  '\033[1;32m'
yellow  =  '\033[1;33m'
blue    =  '\033[1;34m'
magenta =  '\033[1;35m'
cyan    =  '\033[1;36m'
white   =  '\033[1;37m'



print (yellow, 'Welcome to the', green, 'AT command', yellow, 'tester by Daniel Robinson.')
    
def send(cmd, t=0, expect='OK'):
    print(yellow + cmd)
    ser.write(bytes(cmd + '\r', 'utf-8'))
    return receive(t, expect)

def receive(t=0, expect='OK'):
    c = 0
    data = []
    while True:
        d = ser.readline().decode('utf-8')
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
    assert 'OK' in send(cmd, t)

def expect(cmd, reply, t=1):
    data = send(cmd, t, reply)
    assert True in [reply in i for i in data]
    return data
    
@pytest.mark.setup
def test_connect():
    assert ser.is_open == True

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
    receive()

@pytest.mark.setup
def test_COPS():
    expect('AT+COPS=0', '+CEREG: 1', 10)

@pytest.mark.setup
def test_CEREG():
    expect('AT+CEREG?', '+CEREG: 5,1')

@pytest.mark.ping
def test_ping():
    expect('at+nping="8.8.8.8"', '+NPING: "8.8.8.8"', 10)

@pytest.mark.release
def test_release():
    expect('at+cops=2', '+NPSMR: 1', 10)
    expect('at+cops=0', '+CEREG: 1', 10)
    OK('AT+NSOCR="DGRAM",17,14000,1')
    expect('AT+NSOSTF=0,"1.1.1.1",7,0x200,1,"FF"', '+CSCON: 0', 10)
    OK('at+nsocl=0')

@pytest.mark.edrx
def test_eDRX():
    
    for ptw in range(16):
        for edrx in range(10):
            data = expect('AT+NPTWEDRXS=2,5,"' + str(to_bin(edrx, 4)) + '","' + str(to_bin(ptw, 4)) + '"', '+CSCON: 0', 10)
            receive(2)

@pytest.mark.file_edrx
def test_file_eDRX():
    # fileEDRX = open('eDRX ' + time.strftime("%Y%m%d-%H%M%S") + '.log', "w+")
    f = open("nw_edrx.log", "r")
    fx = open('nw_edrx.csv', "w+")
    lines = f.readlines()
    for l in lines:
        print(p.csv(l))
        fx.write(p.csv(l) + '\n')

def test_close():
    ser.close()
    assert ser.is_open == False

if __name__ == '__main__':
    test_close()