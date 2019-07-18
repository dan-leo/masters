from test_ import *

descr = '30_2'

@pytest.mark.skip()
def test_drxset():
    setEDRX(4, 1, 2, 2, 6, 2) # 2.56 continuous

def test_drxcap():
    # capture(12)
    capture(1000, 'drx/' + descr)