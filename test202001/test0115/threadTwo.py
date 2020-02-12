import threading
import time

def chiHuoGuo(people):
    print("%s 吃火锅的小伙伴-羊肉：%s" % (time.ctime(), people))
    time.sleep(1)
    print("%s 吃火锅的小伙伴-鱼丸：%s" % (time.ctime(), people))


class myThread (threading.Thread):   # 继承父类threading.Thread
    def __init__(self, people, name):
        '''重写threading.Thread初始化内容'''
        threading.Thread.__init__(self)
        self.threadName = name
        self.people = people

    def run(self):   # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        '''重写run方法'''
        print("开始线程: " + self.threadName)

        chiHuoGuo(self.people)     # 执行任务
        print("结束线程: " + self.name)


# 创建新线程
thread1 = myThread("xiaoming", "Thread-1")
thread2 = myThread("xiaowang", "Thread-2")

# ============one=============
# 设置子线程为守护线程，线程有一个布尔属性叫做daemon（主线程结束了，子线程必须也跟着结束）
thread1.setDaemon(True)
thread2.setDaemon(True)

# ============one=============
# 阻塞主线程join(timeout)
# 1.如果想让主线程等待子线程结束后再运行的话，就需要用到join(),此方法是在start之后（与setDaemon相反）
# 2.join(timeout)此方法有个timeout参数，是线程超时时间设置。


# 开启线程
thread1.start()
thread2.start()

time.sleep(0.5)
print("退出主线程")
