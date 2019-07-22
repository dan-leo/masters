from process.timing_bits import eDRX_value, paging_time_window, active_time, extended_periodic_TAU

def converter(input_str):
    vendor = 'quectel'
    arr = input_str.split(',')
    # print(arr)
    if 'Bytes=' in input_str:
        return 'Data length: ' + str(uBytes(input_str))
    if '+CEREG: 1' in input_str:
        tau = arr[-1].split('"')
        return 'Active T3324: ' + active_time(arr[-2].split('"')[1]) \
        + ', Periodic T3412: ' + extended_periodic_TAU(tau[1] if len(tau) > 1 else '999')
    if '+NPTWEDRXP' in input_str:
        if vendor == 'ublox':
            # 3, 4
            return 'NW provided eDRX value: ' + eDRX_value(arr[-2].split('"')[1]) \
            + ' seconds, Paging Time Window: ' + paging_time_window(arr[-1].split('"')[1]) \
            + ' seconds'
        elif vendor == 'quectel':
            return 'NW provided eDRX value: ' + eDRX_value(arr[-2]) \
            + ' seconds, Paging Time Window: ' + paging_time_window(arr[-1]) \
            + ' seconds'
    if '+NPTWEDRXS' in input_str:
        if vendor in ['ublox', 'quectel']:
            return 'eDRX value: ' + eDRX_value(arr[-1].split('"')[1]) \
            + ' seconds, Paging Time Window: ' + paging_time_window(arr[-2].split('"')[1]) \
            + ' seconds'
    if '+CPSMS' in input_str:
        if vendor == 'ublox':
            return 'Active T3324: ' + active_time(arr[-1].split('"')[1]) \
            + ', Periodic T3412: ' + extended_periodic_TAU(arr[-2].split('"')[1])
        elif vendor == 'quectel':
            return 'Active T3324: ' + active_time(arr[-1]) \
            + ', Periodic T3412: ' + extended_periodic_TAU(arr[-2])
    return None

print('Input AT strings here:')

try:
    while True:
        raw = input('> ')
        c = converter(raw)
        if (c):
            print(c)
except KeyboardInterrupt as e:
    print('Exiting')