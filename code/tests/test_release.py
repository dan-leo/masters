from test_ import *

@pytest.fixture(autouse=True)
def _config(request):
    pytest.test = 'release/'

# @pytest.mark.skip()
def test_releaseset(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    # setEDRX(0, 0, 2, 1, 6, 1) # 2.56 continuous
    if pytest.vendor == 'simcom':
        setEDRX(0, 9, 0, 1, 2, 31) # off
        return
    setEDRX(0, 9, 0, 0, 0, 0) # off
    capture(1)

def test_release_close(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    expect('at+nsocl=0', '')
    receiveAT(1)

def test_release_release0(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    if pytest.vendor == 'ublox':
        expect('at+nsocl=0', '')
        receiveAT(1)
        OK('AT+NSOCR="DGRAM",17,14000,1')
        receiveAT(1)
        expect('AT+NSOSTF=0,"1.1.1.1",7,0x200,1,"FF"', '+CSCON: 0', 10)
        OK('at+nsocl=0')
    elif pytest.vendor == 'quectel':
        expect('at+nsocl=1', '')
        receiveAT(1)
        OK('AT+NSOCR=DGRAM,17,14000,1')
        expect('AT+NSOSTF=1,1.1.1.1,7,0x200,1,FF', '+CSCON:0', 10)
        OK('at+nsocl=1')
    elif pytest.vendor == 'simcom':
        expect('AT+CSOCL=0', '')
        receiveAT(1)
        OK('AT+RETENTION=1')
        OK('AT+CSOC=1,2,1')
        OK('AT+CSOCON=0,14000,"1.1.1.1"')
        expect('AT+CSOSEND=0,0,"FF"', '', 10)
        OK('AT+CSOCL=0')
    capture(1)

def test_release_release1_(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    if pytest.vendor == 'ublox':
        expect('at+nsocl=0', '')
        receiveAT(1)
        OK('AT+NSOCR="DGRAM",17,14000,1')
        for i in range(1):
            expect('AT+NSOSTF=0,"1.1.1.1",7,0x200,1,"FF"', '+CSCON: 0', 32)
            capture(1)
        OK('at+nsocl=0')
    elif pytest.vendor == 'quectel':
        expect('at+nsocl=1', '')
        receiveAT(1)
        OK('AT+NSOCR=DGRAM,17,14000,1')
        for i in range(1):
            expect('AT+NSOSTF=1,1.1.1.1,7,0x200,1,FF', '+CSCON:0', 32)
            capture(1)
        OK('at+nsocl=1')


def test_release_release16(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    expect('at+nsocl=0', '')
    receiveAT(1)
    for i in range(1):
        OK('AT+NSOCR="DGRAM",17,14000,1')
        expect('AT+NSOSTF=0,"1.1.1.1",7,0x200,16,"FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"', '+CSCON: 0', 32)
        OK('at+nsocl=0')
        capture(1)

def test_release_release64(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    expect('at+nsocl=0', '')
    receiveAT(1)
    for i in range(1):
        OK('AT+NSOCR="DGRAM",17,14000,1')
        expect('AT+NSOSTF=0,"1.1.1.1",7,0x200,64,"FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"', '+CSCON: 0', 32)
        OK('at+nsocl=0')
        capture(1)

def test_release_release128(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    expect('at+nsocl=0', '')
    receiveAT(1)
    for i in range(1):
        OK('AT+NSOCR="DGRAM",17,14000,1')
        expect('AT+NSOSTF=0,"1.1.1.1",7,0x200,128,"FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"', '+CSCON: 0', 32)
        OK('at+nsocl=0')
        capture(1)

def test_release_release256(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    expect('at+nsocl=0', '')
    receiveAT(1)
    for i in range(1):
        OK('AT+NSOCR="DGRAM",17,14000,1')
        expect('AT+NSOSTF=0,"1.1.1.1",7,0x200,256,"FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"', '+CSCON: 0', 32)
        OK('at+nsocl=0')
        capture(1)

def test_release_release512(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    expect('at+nsocl=0', '')
    receiveAT(1)
    for i in range(1):
        OK('AT+NSOCR="DGRAM",17,14000,1')
        expect('AT+NSOSTF=0,"1.1.1.1",7,0x200,512,"FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"', '+CSCON: 0', 32)
        OK('at+nsocl=0')
        capture(1)

# @pytest.mark.skip()
def test_release_capture(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    capture(1)
