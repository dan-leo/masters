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
    mul['010'] = [1, 'deci-hours']
    mul['111'] = [0, 'deactivated']

    if bin_str[:3] in mul:
        t = mul[bin_str[:3]]
        return str(t[0] * int(bin_str[3:], base=2)) + ' ' + t[1]
    return 'failed'

# Paging time window
def paging_time_window(bin_str):
    return str((int(bin_str, base=2) + 1) * 2.56)

# eDRX value
def eDRX_value(bin_str):
    n = int(bin_str, base=2)
    if pytest.vendor == 'ublox':
        if n == 8:
            return '1966.08'
        if n == 9:
            return '2621.44'
        return str(math.pow(2, n) * 10.24)
    elif pytest.vendor == 'quectel':
        if n == 10:
            return '327.68'
        if n == 11:
            return '655.36'
        if n == 12:
            return '1310.72'
        if n == 13:
            return '2621.44'
        if n == 14:
            return '5242.88'
        if n == 14:
            return '10485.76'
        return str((n - 1) * 20.48)
    

def converter(input_str):
    arr = input_str.split(',')
    if 'Bytes=' in input_str:
        return 'Data length: ' + str(uBytes(input_str))
    if '+CEREG: 1' in input_str:
        tau = arr[7].split('"')
        return 'Active T3324: ' + active_time(arr[6].split('"')[1]) \
        + ', Periodic T3412: ' + extended_periodic_TAU(tau[1] if len(tau) > 1 else '999')
    if '+NPTWEDRXP' in input_str:
        return 'NW provided eDRX value: ' + eDRX_value(arr[3].split('"')[1]) \
        + ' seconds, Paging Time Window: ' + paging_time_window(arr[4].split('"')[1]) \
        + ' seconds'
    if '+NPTWEDRXS' in input_str:
        return 'eDRX value: ' + eDRX_value(arr[2].split('"')[1]) \
        + ' seconds, Paging Time Window: ' + paging_time_window(arr[1].split('"')[1]) \
        + ' seconds'
    if '+CPSMS' in input_str:
        if pytest.vendor == 'ublox':
            return 'Active T3324: ' + active_time(arr[-1].split('"')[1]) \
            + ', Periodic T3412: ' + extended_periodic_TAU(arr[-2].split('"')[1])
        elif pytest.vendor == 'quectel':
            print(arr[-1])
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