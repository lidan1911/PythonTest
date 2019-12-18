import time
from functools import wraps

def timeDecorator(func):
    '''timeDecorator的注释'''
    @wraps(func)
    def wrapper():
        '''wrapper的注释'''
        star = time.time()
        f = func()
        end = time.time()
        print('运行时间：%.4f ' % (end-star))
        return f
    return wrapper

@timeDecorator
def methodA():
    '''methodA的注释'''
    print('1、第一个函数')
    time.sleep(0.8)

@timeDecorator
def methodB():
    '''methodB的注释'''
    print('2、第二个函数')
    time.sleep(0.5)

if __name__ == '__main__':
    methodA()
    # methodB()
    print(methodA.__name__)
    print(methodA.__doc__)

