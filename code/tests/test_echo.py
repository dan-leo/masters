from test_ import *

# @pytest.fixture(autouse=True)
# def test_capture(request):
#     pytest.test = 'echo/'
#     tcap(1000)

@pytest.fixture(autouse=True)
def _config(request):
    pytest.test = 'echo/'

@pytest.mark.skip()
def test_echo_set(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    setEDRX(1, 0, 0, 15, 3, 15) # 2.56 cont, 30 sec ptau
    receiveAT(2)
    capture(1)

def test_echo_register(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    flushTIM()
    expect('AT+CFUN=1', 'OK', 3)
    expect('AT+COPS=0', ['+CEREG: 1', '+CSCON: 0'], 300)
    fetchTIM()
    capture(1, 2)


# AT+NSOCR="DGRAM",17,14000
def test_echo(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    if pytest.vendor == 'ublox':
        # expect('at+cops=2', '+NPSMR: 1', 32)
        # expect('at+cops=0', '+CEREG: 1', 32)
        expect('at+nsocl=0', '')
        receiveAT(1)
        OK('AT+NSOCR="DGRAM",17,4444')
        # expect('AT+NSOST=0,"195.34.89.241",7,5,"48656c6c6F"', '+NSONMI: 0', 32)
        # expect('AT+NSOSTF=0,"195.34.89.241",7,0x400,1,"FF"', '+CSCON: 0', 32)
        expect('AT+NSOSTF=0,"34.74.25.60",5555,0x400,3,"313232"', '+NSONMI: 0', 300)
        receiveAT(1, '+CSCON: ')
        OK('AT+NSORF=0,32', 3)
        capture(8, 8)
        receiveAT(20, '+NSONMI: 0')
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

def test_echo_deregister(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    # expect('AT+COPS=2', '+NPSMR:', 100)
    expect('AT+CFUN=0', ['+CSCON: 0', '+CSCON:0', '+NPSMR:'], 20)
    capture(2, 5)
    