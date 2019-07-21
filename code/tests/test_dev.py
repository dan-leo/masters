from test_ import *

# @pytest.fixture(autouse=True)
# def test_capture(request):    pytest.subtest = request.node.name.split('_')[1] + '/'
#     pytest.test = 'dev/'
#     tcap(1000)

@pytest.fixture(autouse=True)
def _config(request):
    pytest.test = 'dev/'

def test_while(request):        
    pytest.subtest = request.node.name.split('_')[1] + '/'
    while True:
        print(pytest.manufacturer)
        time.sleep(1)

def test_OK(request):        
    pytest.subtest = request.node.name.split('_')[1] + '/'
    while True:
        OK('AT')
        time.sleep(1)

def test_devcap(request):        
    pytest.subtest = request.node.name.split('_')[1] + '/'
    capture()

def test_receive(request):        
    pytest.subtest = request.node.name.split('_')[1] + '/'
    while True:
        receiveAT(1)

def test_nuestats(request):
    pytest.subtest = request.node.name.split('_')[1] + '/'
    print(yellow + str(nuestats()))

def test_view(request):
    pytest.subtest = request.node.name.split('_')[1] + '/'
    tPTW = [2.56,5.12,7.68,10.24,12.8,15.36,17.92,20.48,23.04,25.6,28.16,30.72,33.28,35.84,38.4,40.96]
    tEDRX = [10.24, 20.48, 40.96, 81.92, 163.84, 327.68, 655.36, 1310.72, 1966.08, 2621.44]
    tActive = [2, 60, 360, 0]
    tPeriodicTau = [600, 3600, 36000, 2, 30, 60, 1152000, 0]

# 2340,33501,35841,116366.94,108
# 9521,29339,38860,62170.99,127

def test_edrxSet(request):
    pytest.subtest = request.node.name.split('_')[1] + '/'
#     setEDRX(0, 9, 0, 5, 3, 10) # off. drx @104,4.3 ptau 72 drx @87,4.3, ptau 89, drx 70,4.3, ptau 106, drx 53,4.3, ptau 123, drx 36, 4.3, p140, 23.5
#     setEDRX(1, 4, 0, 5, 3, 10) # 20 sec delay. 2 drx. 30 sec ptau
#     setEDRX(0, 0, 0, 5, 3, 10) # 2.56 continuous
#     setEDRX(1, 0, 0, 10, 3, 15) # 2.56 cont, 30 sec ptau
#     setEDRX(0, 0, 0, 0, 3, 2) # 5.5 sec ptau
#     setEDRX(0, 1, 0, 1, 0, 1) # 12 2.56 DRX for 30 sec. silence after
#     setEDRX(0, 2, 0, 15, 3, 20) # one DRX at 20 sec. 30e, 30a, 40p
#     setEDRX(0, 1, 0, 15, 3, 20) # 2, 20, 30, 40 but 2, 30s ptau
    setEDRX(1, 0, 0, 15, 3, 15) # 2.56 cont, 30 sec ptau

def test_change(request):
    pytest.subtest = request.node.name.split('_')[1] + '/'
    print()
    sendTIM('r')
    setEDRX(0, 9, 0, 5, 3, 10) # off

def test_edrxQuery(request):
    pytest.subtest = request.node.name.split('_')[1] + '/'
    edrxQuery()

# https://www.etsi.org/deliver/etsi_TS/125100_125199/125133/13.00.00_60/ts_125133v130000p.pdf
def test_drxlen(request):
    pytest.subtest = request.node.name.split('_')[1] + '/'
    tc = [0.08, 0.16, 0.32, 0.64, 1.28, 2.56, 5.12]
    ti = [0.64, 1.28, 2.56, 5.12]
    pass