import requests

# 通过queryString 方式传递参数给request对象，无论是string还是dic均使用params参数名
# 通过body方式传递参数给request对象，无论是string还是dic均使用data参数名

url = "https://www.cnblogs.com/danmai/ajax/Follow/GetFollowStatus.aspx"
param = "blogUserGuid=3ea8afab-a3eb-e211-8d02-90b11c0b17d6&_=1581944241058"
s = requests.session()
r = s.get(url, params=param)
print("请求返回的数据类型：", type(r))   # <class 'requests.models.Response'>
print("请求返回的数据值：", r)   # <Response [200]>
print("获取内容text：", r.text)   # <a href="javascript:void(0)" onclick="follow('3ea8afab-a3eb-e211-8d02-90b11c0b17d6')">+加关注</a>
print("text内容数据类型string：", type(r.text))  # <class 'str'>
print("======================")


url2 = "https://pagead2.googlesyndication.com/getconfig/sodar"
param = "sv=200&tid=gpt&tv=2020013001&st=env"
param2 = {
    "sv": 200,
    "tid": "gpt",
    "tv": 2020013001,
    "st": "env"
}
# 以上两种参数传递方式均可
r2 = s.get(url2, params=param2)
print("请求返回的数据类型：", type(r2))
print("请求返回的数据值：", r2)
print("接口返回的是字符串或者html：", r2.text)   # json格式的字符串
print("text内容数据类型string：", type(r2.text))  # <class 'str'>
print("请求返回数据转dic：", r2.json())  # 字典
print("请求返回数据转dic后数据类型：", type(r2.json()))  # <class 'dict'>
print("dic获取指定值：", r2.json()["injector_basename"])
print("======================")



# ==================================dic 与json相互转换========================================
import json
dic = {
    "student1": {
        "name": "lidan",
        "age": 20,
        "sex": "女"
    },
    "student2": {
        "name": "zhangsan",
        "age": 15,
        "sex": "男"
    }
}
print("dic类型：", type(dic))  # dic类型： <class 'dict'>
str = json.dumps(dic)  # dic 转 json
print("dict转json后类型：%s，数据值：%s" % (type(str), str))  # dic转json后类型：<class 'str'>，数据值：{"student1": {"name": "lidan", "age": 20, "sex": "\u5973"}, "student2": {"name": "zhangsan", "age": 15, "sex": "\u7537"}}

dic2 = json.loads(str)  # json 转 dic  
print("json转dict后类型：%s，数据值：%s" % (type(dic2), dic2))  # json转dict后类型：<class 'dict'>，数据值：{'student1': {'name': 'lidan', 'age': 20, 'sex': '女'}, 'student2': {'name': 'zhangsan', 'age': 15, 'sex': '男'}}


#  ps: json.load与json.loads    json.dump与json.dumps  区别于功能， 请参考：https://blog.csdn.net/daerzei/article/details/100598901

