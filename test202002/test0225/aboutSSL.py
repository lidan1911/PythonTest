import requests

# ============不开启fiddler，https请求访问正常，没有出现ssl证书问题===============【第一步】
# ============开启fiddler，出现ssl证书问题===============
# s = requests.session()
# url = 'https://www.baidu.com'
# r = s.get(url)
# print(r.status_code)

# ============开启fiddler，出现ssl证书问题===============【第二步】
# 使用verify=False忽略证书验证  ,但是仍然会有一个警告：InsecureRequestWarning
# s = requests.session()
# url = 'https://www.baidu.com'
# r = s.get(url, verify=False)
# print(r.status_code)

# ============开启fiddler，出现ssl证书问题===============【第三步】
# 使用verify=False忽略证书验证  ,但是仍然会有一个警告：InsecureRequestWarning
# 添加如下2行代码忽略警告
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
s = requests.session()
url = 'https://www.baidu.com'
r = s.get(url, verify=False)
print(r.status_code)





