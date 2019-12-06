import base64

# python里面的unicode编码应该是这种格式:\u4e0a\u6d77\u60a0\u60a0
# 这个是\u开头的，里面的英文是小写
# 如果在字符串前面加个u，意思是转化成unicode编码
# python3默认的编码就是unicode编码,在python中的名称是unicode_escape
# decode英文意思是 解码，encode英文原意 编码


str = "%u6b6a%u8116%u5b50%u59d0%u59d0"
s = str.replace('%', '\\')
print(s.encode('utf-8').decode('unicode_escape'))
