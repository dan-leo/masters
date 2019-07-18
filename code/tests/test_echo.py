from test_ import *

@pytest.fixture(autouse=True)
def test_capture():
    pytest.test = 'echo/'
    tcap(1000)

@pytest.mark.skip()
def test_echoset():
    pytest.subtest = 'set/'
    setEDRX(1, 0, 0, 15, 3, 15) # 2.56 cont, 30 sec ptau
    receiveAT(2)


# AT+NSOCR="DGRAM",17,14000
def test_echo():
    pytest.subtest = ''
    if pytest.vendor == 'ublox':
        # expect('at+cops=2', '+NPSMR: 1', 32)
        # expect('at+cops=0', '+CEREG: 1', 32)
        expect('at+nsocl=0', '')
        receiveAT(1)
        OK('AT+NSOCR="DGRAM",17,4444')
        # expect('AT+NSOST=0,"195.34.89.241",7,5,"48656c6c6F"', '+NSONMI: 0', 32)
        # expect('AT+NSOSTF=0,"195.34.89.241",7,0x400,1,"FF"', '+CSCON: 0', 32)
        expect('AT+NSOSTF=0,"34.74.25.60",5555,0x400,3,"313232"', '+NSONMI: 0', 32)
        receiveAT(1, '+CSCON: ')
        OK('AT+NSORF=0,32', 3)
        receiveAT(300, '+NSONMI: 0')
        OK('AT+NSORF=0,32', 3)
        # OK('at+nsocl=0')
        # capture(1, 'echo/' + descr)
    elif pytest.vendor == 'simcom':
        expect('AT+CSOCL=0', '')
        receiveAT(1)
        OK('AT+RETENTION=1')
        # OK('AT+CSOC=1,1,1')
        # OK('AT+CSOCON=0,30000,"52.20.16.20"')
        OK('AT+CSOC=1,2,1')
        OK('AT+CSOCON=0,5555,"34.74.25.60"')
        # OK('AT+CSOC=1,2,1')
        # OK('AT+CSOCON=0,7,"195.34.89.241"')
        expect('AT+CSOSEND=0,0,"ABCDE12345d"', '+CSONMI: 0', 32)
        # OK('AT+CSOCL=0')
    