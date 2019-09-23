from test_ import *

# @pytest.mark.setup
# def test_connect(request):
# pytest.subtest = request.node.name.split('_'-)[1] + '/'
#     assert serAT.is_open == True

@pytest.fixture(autouse=True)
def _config(request):
    pytest.test = 'setup/'

def test_serial(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    import serial.tools.list_ports
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))
        print(hwid.split('=')[1].split()[0])

@pytest.mark.setup
def test_AT(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    print(pytest.vendor)
    OK('AT')

@pytest.mark.setup
def test_NCONFIG(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    if pytest.vendor in ['ublox', 'quectel']:
        OK('AT+NCONFIG="AUTOCONNECT","FALSE"')
        OK('AT+NCONFIG="CR_0859_SI_AVOID","TRUE"')
        OK('AT+NCONFIG="CR_0354_0338_SCRAMBLING","TRUE"')

@pytest.mark.setup
def test_URC(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    if pytest.vendor in ['ublox', 'quectel']:
        OK('AT+CMEE=1')
        OK('AT+NPSMR=1')
        OK('AT+CSCON=1')
    if pytest.vendor in ['ublox', 'simcom']:
        OK('AT+CEREG=5')
    if pytest.vendor == 'quectel':
        OK('AT+CEREG=3')
    if pytest.vendor == 'simcom':
        OK('AT+CGEREP=1')
        OK('AT+CGREG=2')
        OK('AT+CREG=2')
        OK('AT+CTZR=1')
        OK('AT+CCIOTOPT=1')
        OK('AT+CLTS=1')
        OK('AT+CSMINS=1')
        OK('AT+CPSMSTATUS=1')
        OK('ATE0')
    # todo: at+natspeed=115200,30,1


# @pytest.mark.skip()
@pytest.mark.apn
def test_APN(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    apn = 'rflab'
    # apn = 'nbiot.vodacom.za'
    
    if pytest.vendor in ['ublox', 'quectel']:
        OK('AT+CGDCONT=0,"IP","' + apn + '"')
    elif pytest.vendor == 'simcom':
        OK('AT*MCGDEFCONT="IP","' + apn + '"')

@pytest.mark.setup
def test_CFUN(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    OK('AT+CFUN=0', 3)
    receiveAT(1)
    expect('at+cfun?', '+CFUN:', 1)
    receiveAT(1)
    expect('AT+CFUN=1', '+CEREG:', 2)
    receiveAT(1)

@pytest.mark.setup
def test_COPS(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    if pytest.vendor in ['ublox', 'quectel']:
        receiveAT(3)
    if pytest.vendor == 'simcom':
        expect('AT+COPS=0', '+CEREG: 1', 10)
        return
    expect('AT+COPS=0', ['+CEREG: 1', '+CEREG:1'], 10)

@pytest.mark.setup
def test_CEREG(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    expect('AT+CEREG?', ['+CEREG: 5,1', '+CEREG:3,1'])

@pytest.mark.setup
def test_ping(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    if pytest.vendor in ['ublox', 'quectel']:
        expect('at+nping="8.8.8.8"', ['+NPING: "8.8.8.8"', '+NPING:8.8.8.8', '+NPINGERR:'], 20)
    if pytest.vendor == 'simcom':
        expect('AT+CIPPING="8.8.8.8"', '+CIPPING:', 20)
        receiveAT(10, '+CIPPING:')
        receiveAT(10, '+CIPPING:')
        receiveAT(10, '+CIPPING:')
    print(nuestats())
    print('### 0')

# @pytest.mark.release
# def test_release(request):
#     pytest.subtest = request.node.name.split('_')[-1] + '/'
#     # expect('at+cops=2', '+NPSMR: 1', 10)
#     # expect('at+cops=0', '+CEREG: 1', 10)
#     OK('AT+NSOCR="DGRAM",17,14000,1')
#     expect('AT+NSOSTF=0,"1.1.1.1",7,0x200,1,"FF"', '+CSCON: 0', 10)
#     OK('at+nsocl=0')

@pytest.mark.reboot
def test_reboot(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    expect('at+nrb', '')

def test_edrxset2(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    setEDRX(0, 5, 0, 0, 0, 0) # 2.56 continuous
    capture(1)