from test_ import *

@pytest.fixture(autouse=True)
def _config(request):
    pytest.test = 'cops/'

# @pytest.mark.skip()
def test_cops_set(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    # setEDRX(0, 0, 2, 1, 6, 1) # 2.56 continuous
    setEDRX(0, 9, 0, 0, 0, 0) # off
#     capture(1)

############## 10 sec ##############

@pytest.mark.reg1
def test_cops_cfun1(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    flushTIM()
    # expect('AT+COPS=2', '+NPSMR:', 100)
    reply = OK('AT+CFUN=0', 3)
    if '+CSCON:' in receiveAT(3) or '+CSCON:' in reply:
        fetchTIM()
        capture(1, 3)

@pytest.mark.reg1
def test_cops_register1(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    flushTIM()
    expect('AT+CFUN=1', 'OK', 3)
    expect('AT+COPS=0', '')
    receiveAT(300, ['+CEREG: 1', '+CSCON: 0'])
#    pauseTIM(True)

@pytest.mark.reg1
def test_cops_delay(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    print('Delay initiated.')
    capture(3, 10)
    print('Delay ended.')

@pytest.mark.reg1
def test_cops_tensec(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    # expect('AT+COPS=2', '+NPSMR:', 100)
    expect('AT+CFUN=0', '+CSCON: 0', 3)
    capture(2, 5)

############## reg release ##############

@pytest.mark.reg2
def test_cops_register2(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    flushTIM()
    expect('AT+CFUN=1', 'OK', 3)
    expect('AT+COPS=0', ['+CEREG: 1', '+CSCON: 0'], 300)
#    pauseTIM(True)

@pytest.mark.reg2
def test_cops_release(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    receiveAT(1)
    fetchTIM()
    capture(1, 3)
    expect('at+nsocl=0', '')
    receiveAT(1)
    OK('AT+NSOCR="DGRAM",17,14000,1')
    receiveAT(1)
    expect('AT+NSOSTF=0,"1.1.1.1",7,0x200,1,"FF"', '+CSCON: 0', 100)
    OK('at+nsocl=0')
    receiveAT(1)
    receiveAT(2)
    fetchTIM()
    capture(1, 3)

############## dereg release ##############

@pytest.mark.reg3
def test_cops_deregister(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
#     time.sleep(5)
#     receiveAT(5)
    OK('AT+COPS=2', 5)
##     pauseTIM(True)
    receiveAT(300, '+NPSMR:')
##     pauseTIM(False)
#     expect('AT+CFUN=0', '', 1)
#     receiveAT(3)
#     fetchTIM()
    flushTIM()
    capture(1, 3)
#     capture(1, 3)

############## inactive ##############

@pytest.mark.inactive
def test_cops_inactive(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    # primeTIM(False)
    expect('AT+CFUN=0', '')
    receiveAT(5)
    expect('AT+CFUN=1', 'OK', 3)
    expect('AT+COPS=0', ['+CEREG: 1', '+CSCON: 0'], 300)
#     capture(1, 400)
