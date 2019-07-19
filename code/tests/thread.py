import time

def fed():
    try:
        var = True
        while var:
            print('yop')
            time.sleep(1)
            var = False
        else:
            print('nop')
            return
    finally:
        print('ziod')

fed()


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