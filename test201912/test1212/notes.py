
'''模块，注释内容'''
class testClass():
    '''类注，释内容'''
    def testMethod(self):
        '''方法，注释内容'''
        print('====')

print(__doc__)
print(testClass.__doc__)
print(testClass.testMethod.__doc__)


