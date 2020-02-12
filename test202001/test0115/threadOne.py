import threading
import time

def chi(threadName,name):
    print("%s 吃着%s开始：" % (time.ctime(), threadName))
    print("%s 吃着火锅：涮羊肉" % time.ctime())
    time.sleep(1)
    time.sleep(1)
    print("%s 吃着火锅：涮牛肉" % time.ctime())
    time.sleep(1)
    print("%s 吃着火锅：贡丸" % time.ctime())
    time.sleep(1)
    print("%s 吃着%s结束--" % (time.ctime(),threadName))
    print("%s 运行结束！"%name)


def ting(threadName):
    print("%s 哼着%s1！" % (time.ctime(),threadName))
    time.sleep(2)
    print("%s 哼着小曲2！" % time.ctime())
    time.sleep(2)
    print("%s 哼着小曲3！" % time.ctime())
    time.sleep(2)
    print("%s 哼着小曲4！" % time.ctime())
    time.sleep(2)
    print("%s 哼着小曲5！" % time.ctime())
    time.sleep(2)

# 创建线程数组
threads = []
# 创建线程t1，并添加到线程数组，数组只有一个数据需要最后加逗号，否则会当做字符串处理，出现异常
t1 = threading.Thread(target=chi, args=("火锅", "吃火锅"))

# 传kwargs参数
# t1 = threading.Thread(target=chi, kwargs={"threadName": "火锅", "name": "吃火锅"})

threads.append(t1)
# 创建线程t2，并添加到线程数组
t2 = threading.Thread(target=ting, args=("小曲",))
threads.append(t2)


if __name__ == '__main__':
    # 启动线程
    for t in threads:
        t.start()
