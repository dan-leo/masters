from process.globals import *

## T3412
def extended_periodic_TAU(bin_str):
    mul = {}
    mul['000'] = [10, 'minutes']
    mul['001'] = [1, 'hours']
    mul['010'] = [10, 'hours']
    mul['011'] = [2, 'seconds']
    mul['100'] = [30, 'seconds']
    mul['101'] = [1, 'minutes']
    mul['110'] = [320, 'hours']
    mul['111'] = [0, 'deactivated']

    if bin_str[:3] in mul:
        t = mul[bin_str[:3]]
        return str(t[0] * int(bin_str[3:], base=2)) + ' ' + t[1]
    return 'failed'

## T3324
def active_time(bin_str):
    mul = {}
    mul['000'] = [2, 'seconds']
    mul['001'] = [1, 'minutes']
    mul['010'] = [6, 'minutes']
    mul['111'] = [0, 'deactivated']

    if bin_str[:3] in mul:
        t = mul[bin_str[:3]]
        return str(t[0] * int(bin_str[3:], base=2)) + ' ' + t[1]
    return 'failed'

# Paging time window
def paging_time_window(bin_str):
    return str((int(bin_str, base=2) + 1) * 2.56)

# eDRX value
# http://www.microchip.ua/simcom/LTE/SIM7020/AppNotes/SIM7020%20Series_Low%20Power%20Mode_Application%20Note_V1.03.pdf
# https://www.etsi.org/deliver/etsi_TS/125100_125199/125133/13.00.00_60/ts_125133v130000p.pdf
def eDRX_value(bin_str, mode='wb-s1'):
    n = int(bin_str, base=2)
    if mode == 'nb-s1':
        if n < 2:
            return 'unchanged'
        if n in [4, 6, 7, 8]:
            return '20.48'
    if mode == 'wb-s1':
        if n in [14, 15]:
            return '2621,44'
    if n == 0:
        return '5.12'
    if n == 1:
        return '10.24'
    if n < 9:
        return str((n - 1) * 20.48)
    if n < 16:
        return str(math.pow(2, n - 5) * 10.24)
    

def converter(input_str):
    arr = input_str.split(',')
    # print(arr)
    if 'Bytes=' in input_str:
        return 'Data length: ' + str(uBytes(input_str))
    if '+CEREG: 1' in input_str:
        tau = arr[-1].split('"')
        return 'Active T3324: ' + active_time(arr[-2].split('"')[1]) \
        + ', Periodic T3412: ' + extended_periodic_TAU(tau[1] if len(tau) > 1 else '999')
    if '+NPTWEDRXP' in input_str:
        return 'NW provided eDRX value: ' + eDRX_value(arr[3].split('"')[1]) \
        + ' seconds, Paging Time Window: ' + paging_time_window(arr[4].split('"')[1]) \
        + ' seconds'
    if '+NPTWEDRXS' in input_str:
        return 'eDRX value: ' + eDRX_value(arr[-1].split('"')[1]) \
        + ' seconds, Paging Time Window: ' + paging_time_window(arr[-2].split('"')[1]) \
        + ' seconds'
    if '+CPSMS' in input_str:
        if pytest.vendor == 'ublox':
            return 'Active T3324: ' + active_time(arr[-1].split('"')[1]) \
            + ', Periodic T3412: ' + extended_periodic_TAU(arr[-2].split('"')[1])
        elif pytest.vendor == 'quectel':
            return 'Active T3324: ' + active_time(arr[-1]) \
            + ', Periodic T3412: ' + extended_periodic_TAU(arr[-2])
    return None

def csv(input_str):
    arr = input_str.split(',')
    # if 'Bytes=' in input_str:
    #     return 'Data length: ' + str(uBytes(input_str))
    # if '+CEREG: 1' in input_str:
    #     return 'Active T3324: ' + active_time(arr[7].split('"')[1]) \
    #      + ', Periodic T3412: ' + extended_periodic_TAU(arr[8].split('"')[1]) if len(arr) > 7 else 'empty'
    if '+NPTWEDRXP' in input_str:
        return 'eDRX,PTW,NW eDRX,NW PTW,' \
            + arr[2] + ',' + arr[1] + ',' + arr[3] + ',' + arr[4].strip() + ',' \
            + eDRX_value(arr[2].split('"')[1]) + ',' + paging_time_window(arr[1].split('"')[1]) + ',' \
            + eDRX_value(arr[3].split('"')[1]) + ',' + paging_time_window(arr[4].split('"')[1])
    if '+NPTWEDRXS' in input_str:
        return 'eDRX value: ' + eDRX_value(arr[2].split('"')[1]) \
         + ' seconds, Paging Time Window: ' + paging_time_window(arr[1].split('"')[1]) \
         + ' seconds'
    # if '+CPSMS' in input_str:
    #     return 'Active T3324: ' + active_time(arr[-1].split('"')[1]) \
    #      + ', Periodic T3412: ' + extended_periodic_TAU(arr[-2].split('"')[1])
    return None