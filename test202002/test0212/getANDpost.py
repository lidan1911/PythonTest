import requests

#================================   http   get请求   =====================================

# 简单get请求
url = "https://www.baidu.com"
r = requests.get(url)
print("get==code=", r.status_code)
print("get==text=", r.text)

# 带参数的get请求
url2 = "http://ctc-api.test.daqsoft.com/v2/res/api/scenic/getApiScenicList"
param = "siteCode=site844810&type=&crowd=&level=&region=&keyword=&areaSiteSwitch=&sortType=disNum&lng=104.07196&lat=30.53777&currPage=1&pageSize=10"
r2 = requests.get(url2, param)
print("带参数的get请求，返回状态码：", r2.status_code)
print("=========", r2.json())
print("=========", r2.json()["message"])


# -- r.status_code     #响应状态码
# -- r.content           #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
# -- r.headers          #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
# -- r.json()             #Requests中内置的JSON解码器
# -- r.url                  # 获取url
# -- r.encoding         # 编码格式
# -- r.cookies           # 获取cookie
# -- r.raw                #返回原始响应体
# -- r.text               #字符串方式的响应体，会自动根据响应头部的字符编码进行解码
# -- r.raise_for_status() #失败请求(非200响应)抛出异常

#================================   http   get请求   =====================================


print("=====================")
help(requests)  # 可以查看post请求基础示例










