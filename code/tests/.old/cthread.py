#!/usr/bin/python3

import serial, time, sys, threading
from colorama import Fore, Style, init as colorama_init

colorama_init()

# lock to serialize console output
lock = threading.Lock()

# class Highlight:
#   def __init__(self, clazz, color):
#     self.color = color
#     self.clazz = clazz
#   def __enter__(self):
#     print(self.color, end="")
#   def __exit__(self, type, value, traceback):
#     if self.clazz == Fore:
#       print(Fore.RESET, end="")
#     else:
#       assert self.clazz == Style
#       print(Style.RESET_ALL, end="")
#     sys.stdout.flush()

data = False

if len(sys.argv) != 3 and len(sys.argv) != 4:
  sys.stderr.write("Usage: %s <baud> <port1> [<port2>]\n" % (sys.argv[0]))
  exit(1)

def read_serial(port, baud, color):
  ser = serial.Serial()
  ser.port = port

  ser.baudrate = baud
  ser.bytesize = serial.EIGHTBITS #number of bits per bytes
  ser.parity = serial.PARITY_NONE #set parity check: no parity
  ser.stopbits = serial.STOPBITS_ONE #number of stop bits
  #ser.timeout = None          #block read
  ser.timeout = 0            # non blocking read
  ser.xonxoff = False     #disable software flow control
  ser.rtscts = False     #disable hardware (RTS/CTS) flow control
  ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
  ser.writeTimeout = 1     #timeout for write

  global data

  stream = []
  
  try:
    ser.open()
  except Exception as e:
    print("error open serial port: " + str(e))
    exit()

  if ser.isOpen():
    try:
        while True:
            if data:
                data = False
                print(Fore.YELLOW + 'at+nuestats="RADIO"' + Fore.WHITE)
                ser.write('at+nuestats="ALL"\r\n'.encode())
                print(Fore.CYAN)
            c = ser.read(size=2024).decode('utf-8').strip()
            # c = ser.readline()
            # c = c.strip()
            with lock:
              if len(c) > 0:
                #   c = c
                  stream.append(c)
                  if 'OK' in c:
                      print(len(stream), stream)
                      stream = []
                  print(color + c)
                #   if not 'NUESTATS' in c:
                #     print(color + c)
                #   print(port)
                  if port != 'COM108':
                      data = True
                    # write_serial('COM108', 115200, Fore.YELLOW, 'at+nuestats="ALL"\r\n'.encode())
                # print()
                # print(color)
                # sys.stdout.buffer.write(c)

        ser.close()

    except Exception as e1:
        print ("error communicating...: " + str(e1))

  else:
    print("cannot open serial port ")
    exit()

# Create two threads as follows
try:
   t = threading.Thread(target=read_serial, args=(sys.argv[2], sys.argv[1], Fore.GREEN ))
   t.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
   t.start()

   if len(sys.argv) == 4:
      t = threading.Thread(target=read_serial, args=(sys.argv[3], sys.argv[1], Fore.RED ))
      t.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
      t.start()
except:
   print("Error: unable to start thread")

try:
   while True:
      pass
except KeyboardInterrupt:
   exit()


# #!/usr/bin/env python3

# import concurrent.futures
# import time

# def func_that_raises(do_raise):
#     for i in range(3):
#         print(i)
#         time.sleep(0.1)
#     if do_raise:
#         raise Exception()
#     for i in range(3):
#         print(i)
#         time.sleep(0.1)

# with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#     futures = []
#     futures.append(executor.submit(func_that_raises, False))
#     futures.append(executor.submit(func_that_raises, True))
#     for future in concurrent.futures.as_completed(futures):
#         print(repr(future.exception()))

# import time

# def fed():
#     try:
#         var = True
#         while var:
#             print('yop')
#             time.sleep(1)
#             var = False
#         else:
#             print('nop')
#             return
#     finally:
#         print('ziod')

# fed()


# from test_ import *

# serialOpen()
# thread = threading.Thread(target=capture)
# thread.daemon=True
# thread.start()
# while True:
#     print('test')
#     time.sleep(1)
# serialClose()


# for i in range(5):
#     print(i)
#     break
# else:
#     print(9)


# import threading
# import time
# import inspect

# class Thread(threading.Thread):
#     def __init__(self, t, *args):
#         threading.Thread.__init__(self, target=t, args=args)
#         self.start()

# count = 0
# lock = threading.Lock()

# def incre():
#     global count
#     caller = inspect.getouterframes(inspect.currentframe())[1][3]
#     print("Inside %s()" % caller)
#     print("Acquiring lock")
#     with lock:
#         print("Lock Acquired")
#         count += 1  
#         time.sleep(2)  

# def bye():
#     while count < 5:
#         incre()

# def hello_there():
#     while count < 5:
#         incre()

# def main():    
#     hello = Thread(hello_there)
#     goodbye = Thread(bye)


# if __name__ == '__main__':
#     main()