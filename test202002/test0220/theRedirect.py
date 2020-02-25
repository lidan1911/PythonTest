import requests

url = "https://i.cnblogs.com/EditPosts.aspx?opt=1"

s = requests.session()

r = s.get(url, verify=False, allow_redirects=False)   # 设置不允许重定向
print(r.status_code)   # 302  若请求不设置allow_redirects=False，，会自动重定向，获取不到实际请求结果信息，获取的status_code会输出200

# 有以上请求信息，接下来可以获取重定向后的地址【在第一个请求后，服务器会下发一个新的请求链接，在response的headers里】
# print("r.headers信息：", r.headers)
# print("获取r.headers里面的重定向地址：", r.headers["Location"])


print("r.headers信息：%s \n获取r.headers里面的重定向地址：%s" % (r.headers, r.headers["Location"]))
print("===")

