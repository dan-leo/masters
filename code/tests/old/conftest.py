# pytest_plugins = 'pytest_session2file'

# from _pytest.cacheprovider import Cache
# from collections import defaultdict

# import _pytest.cacheprovider
# import pytest

# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     config.cache = Cache(config)
#     config.cache.set('record_s', defaultdict(list))

# @pytest.fixture(autouse=True)
# def record(request):
#     cache = request.config.cache
#     record_s = cache.get('record_s', {})
#     testname = request.node.name
#     # Tried to avoid the initialization, but it throws errors.
#     record_s[testname] = []
#     yield record_s[testname]
#     cache.set('record_s', record_s)

# @pytest.hookimpl(trylast=True)
# def pytest_unconfigure(config):
#     print("====================================================================\n")
#     print("\t\tTerminal Test Report Summary: \n")
#     print("====================================================================\n")
#     r_cache = config.cache.get('record_s',{})
#     print(str(r_cache))