print('Welcome to AT command interface to testing-framework\n')

ip = "8.8.8.8"

# +QPING: 0,"8.8.8.8",32,484,255
# +QPING: 0,10,10,0,169,485,245

while True:
    s = input()

    if 'AT+' not in s:
        if '+QPING' in s:
            if ip in s:
                print('ping time:', s.split(',')[-2])

    print('OK')
