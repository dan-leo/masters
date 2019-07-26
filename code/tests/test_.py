from __future__ import print_function
from process.globals import *   

# def pytest_configure():

def setup_module(module):
    pytest.vendor = 'vendor_undef'
    serialOpen()
    print()

    # pytest.manufacturer = 'huawei'
    # pytest.manufacturer = 'ericsson'
    # pytest.manufacturer = 'nokia'
    pytest.manufacturer = 'zte'

    # pytest.loc = 'vodacom/cticc/'
    # pytest.loc = 'vodacom/centurycity/'
    # pytest.loc = 'mtn/mil_lab/'
    pytest.loc = 'mtn/rf_shield/'

    # pytest.descr = '0_slightly_open'
    # pytest.descr = '10_slightly_open'
    # pytest.descr = '20_slightly_open'
    # pytest.descr = '30_slightly_open'
    # pytest.descr = '40_slightly_open'
    # pytest.descr = '50_slightly_open'    
    # pytest.descr = '60_slightly_open'
    # pytest.descr = '70_slightly_open'
    # pytest.descr = '80_slightly_open'
    # pytest.descr = '90_slightly_open'
    # pytest.descr = '100_slightly_open'
    pytest.descr = '110_slightly_open'

    pytest.test = 'dump/'
    pytest.subtest = ''

    # pytest.lock = threading.Lock()
 
def teardown_module(module):
    serialClose()