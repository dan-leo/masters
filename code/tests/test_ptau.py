from test_ import *

descr = '50'

@pytest.fixture(autouse=True)
def _config(request):
    pytest.test = 'ptau/'

# @pytest.mark.skip()
def test_ptauset(request):
    setEDRX(4, 1, 0, 0, 3, 2) # 5.5 sec ptau

def test_ptau(request):
    capture(1000, 'ptau/' + descr)