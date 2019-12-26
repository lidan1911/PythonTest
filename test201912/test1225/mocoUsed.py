import unittest
import requests

'''
利用moco模拟接口相应数据，Python requests+unittest写一个简单的接口测试用例
1、下载moco文件jar包moco-runner-0.12.0-standalone.jar（当前放在路径D:\Program File\Instrall File\moco下）
2、新建json文件与jar放在相同路径下
3、cmd，进入到jar包路径下，执行：java -jar moco-runner-0.12.0-standalone.jar http -p 6666 -c json文件名.json  (说明：http代表协议，-p端口号，-c配置文件)
4、浏览器（火狐、谷歌访问不到）or第三方工具（postman、jmeter等）访问，http://localhost:6666/api/hello 可以查看到返回值
'''

class MocoTestApi(unittest.TestCase):
    def setUp(self):
        self.url = "http://localhost:6666"
        
    def test_moco_test_api(self):
        api = '/api/hello'
        url = self.url + api
        r = requests.get(url)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.text, 'hello Savitar!')
        
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()