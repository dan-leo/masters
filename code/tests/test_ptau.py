from test_ import *

descr = '50'

@pytest.fixture(autouse=True)
def _config(request):
    pytest.test = 'ptau/'

# @pytest.mark.skip()
def test_ptau_set(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    setEDRX(4, 1, 0, 0, 3, 2) # 5.5 sec ptau
    capture(1)

def test_ptau_capture(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    capture()