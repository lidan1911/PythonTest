
# # globals() 函数简单使用（各用例间可以使用globals()传递参数值）
# # print(globals())
# # globals()['a'] = 5
# # b = globals()['a']
# # print(b)

import unittest

'''
多个用例之间都用globals()函数，势必会赵成很混乱，若需要传递的参数过多
因此，可以吧globals()放到函数setUp里面，定义为全局变量，然后需要设置的手调用配置值即可，达到同一变量名称，多次使用，方便管理
'''

class GlobalsFunc(unittest.TestCase):

    def setUp(self):
        self.pub = globals()

    def test_a(self):
        self.pub['a'] = 1
        print('=====test_a====')

    def test_b(self):
        self.pub['b'] = 2
        print('=====test_b====')

    def test_c(self):
        c = self.pub['a'] + self.pub['b']
        print("=====test_c====,c==", c)

if __name__ == '__main__':
    unittest.main()


