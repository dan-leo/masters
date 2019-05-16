import unittest
import serial
from time import sleep

ser = serial.Serial('COM38', 9600, timeout=1)

class Process:
    def __init__(self, ser):
        self.ser = ser
    
    def send(self, cmd, t=1):
        self.ser.write(bytes(cmd + '\r', 'utf-8'))
        return self.receive(t)

    def receive(self, t=1):
        data = []
        c = 0
        print(t)
        while True:
            if c == t:
                return ['timeout']
            d = self.ser.readline().decode('utf-8')
            if len(d) == 0:
                c += 1
                continue
            d = d.strip()
            if len(d) > 0:
                data.append(d)
            if 'OK' in d or 'ERROR' in d:
                return data
    
    def OK(self, cmd):
        self.send(cmd)
        ser.readline()
        return ser.readline()

class TestSetup(unittest.TestCase):

    def test2_OK(self, cmd='OK'):
        print(cmd)
        self.assertEqual(p.send(cmd, 1)[-1], 'OK', "Should print OK")
        
    def test1_connect(self):
        self.assertEqual(ser.is_open, True)

##    def test2_AT(self):
##        self.OK('OK')

    def test3_URC(self):
        ser.write(b'AT\r')
        ser.readline()
        self.assertEqual(ser.readline()[:2], b'OK', "Should print OK")

    def test99_close(self):
        ser.close()
        self.assertEqual(ser.is_open, False)

if __name__ == '__main__':
    p = Process(ser)
    unittest.main()
