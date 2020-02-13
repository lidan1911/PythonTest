import requests

s = requests.session()
r = s.get("https://www.baidu.com", verify=True)
print(r.text)

print("================")
print(help(requests.session()))
