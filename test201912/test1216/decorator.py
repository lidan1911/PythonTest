import time

def timeDecorator(func):
    def wrapper():
        star = time.time()
        f = func()
        end = time.time()
        print('运行时间：%.4f ' % (end-star))
        return f
    return wrapper

@timeDecorator
def methodA():
    print('1、第一个函数')
    time.sleep(0.8)

@timeDecorator
def methodB():
    print('2、第二个函数')
    time.sleep(0.5)

if __name__ == '__main__':
    methodA()
    methodB()
