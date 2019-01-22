# import time
#
# def timi(f):
#     def inner():
#         start_time = time.time()
#         f()
#         end_time = time.time()
#         print(end_time - start_time)
#     return inner
#
# @timi
# def func():
#     time.sleep(1)
#     print('复杂')
#
# func()

import time

def timi(f):
    def inner(*args,**kwargs):
        start_time = time.time()
        f(*args,**kwargs)
        end_time = time.time()
        print(end_time - start_time)
    return inner

@timi
def func(a,b):
    time.sleep(1)
    print('复杂 %s %s ' % (a,b))

@timi
def fun1(*args,**kwargs):
    time.sleep(1)
    print('args:',args)
    print('kwargs:',kwargs)

# func('barry','alex')
fun1(1,2,3,name='barry',age=18)
