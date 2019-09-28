from test_ import *

@pytest.fixture(autouse=True)
def _config(request):
    pytest.test = 'drx/'

# @pytest.mark.skip()
def test_drx_set(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    setEDRX(4, 1, 2, 5, 6, 2) # 2.56 continuous
    # setEDRX(4, 1, 2, 5, 6, 2) # 2.56 continuous
    capture(1)

def test_drx_cap(request):
    pytest.subtest = request.node.name.split('_')[-1] + '/'
    # capture(10)
    capture(10000)