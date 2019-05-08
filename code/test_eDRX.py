import unittest
import serial
from time import sleep

ser = serial.Serial('COM38', 9600, timeout=1)
    
def send(cmd, t=5):
    ser.write(bytes(cmd + '\r', 'utf-8'))
    return receive(t)

def receive(t):
    data = []
    c = 0
    while True:
        if c == t:
            return ['timeout']
        d = ser.readline().decode('utf-8')
        if len(d) == 0:
            c += 1
            continue
        d = d.strip()
        if len(d) > 0:
            data.append(d)
        if 'OK' in d or 'ERROR' in d:
            return data

def OK(cmd):
    assert send(cmd)[-1] == 'OK'

def expect(cmd, reply, pos=-2):
    assert send(cmd)[pos] == reply
    
def test_connect():
    assert ser.is_open == True

def test_AT():
    OK('AT')

def test_URC():
    OK('AT+CMEE=1')
    OK('AT+CSCON=1')
    OK('AT+CEREG=5')
    OK('AT+NPSMR=1')

def test_CFUN():
    expect('AT+CFUN?', '+CFUN: 0')
    expect('AT+CFUN=1', '+CFUN: 0')

def test_close():
    ser.close()
    assert ser.is_open == False

if __name__ == '__main__':
    print(send('at+cops?'))
    print(send('at+cfun=1', 2))
    test_close()