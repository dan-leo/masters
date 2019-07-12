from __future__ import print_function
from process.globals import *

import pytest

def pytest_configure():
    pytest.vendor = 'pytest'

def setup_module(module):
    serialOpen()
    print()
 
def teardown_module(module):
    serialClose()