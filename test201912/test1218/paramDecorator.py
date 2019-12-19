import time


def runtime(slowly=1):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            start = time.time()
            f = func(*args, **kwargs)     # 原函数
            end = time.time()
            t = end-start
            time.sleep((slowly-1)*t)  # 延迟效果
            new_end = time.time()
            print("运行时长：%.4f 秒" % (new_end-start))
            return f
        return inner_wrapper
    return wrapper


@runtime(1.5)
def func_a(a):
    print("hello"+a)
    time.sleep(0.5)


@runtime(1.5)
def func_b(b, c="xx"):
    print("world"+b+c)
    time.sleep(0.8)


if __name__ == '__main__':
    func_a("a")
    func_b("b", c="xxx")