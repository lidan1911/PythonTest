
class A(object):
    def __init__(self, param=1):
        self.param = param

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print('前期操作')
            print('参数=', self.param)
            # print("==========", **kwargs)
            # print('dic参数：', **kwargs)
            f = func(*args, **kwargs)
            print('后期操作')
            return f
        return wrapper

@A(2)
def methodA(a):
    print('methodA方法内输出：', a)

@A(3)
def methodB(b):
    print('methodB方法内输出：', b)

@A(4)
def methodC(c, d='3', e='4'):
    print('methodC方法内输出：', c+d+e)


if __name__ == '__main__':
    # methodA(2)
    # methodB(3)
    methodC('hello', d=' word', e=' !')
