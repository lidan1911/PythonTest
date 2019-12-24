from unittest import mock
import unittest

class SubClass(object):
    def add(self, a, b):
        '''两个数相加'''
        print('=========')
        return a+b

class TestSub(unittest.TestCase):
    '''测试两个数相加用例'''
    def test_sub(self):
        model = SubClass()
        model.add = mock.Mock(return_value=10, side_effect=model.add)  # 传递side_effect关键字参数, 会覆盖return_value参数值, 使用真实的add方法测试
        result = model.add(5, 5)
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()