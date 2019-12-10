
# ===常用range使用===
a = range(1, 11)
print(a)
print(type(a))
b = list(a)
print(b)

# ===列表生成器(原序列不变)===

li = list(range(1, 11))
li1 = [x*2 for x in li]
print('初始序列：', li)
print('X2后的序列：', li1)

# 融入if判断，筛选大于5的数
li2 = [x for x in li if x > 5]
print('序列中大于5的数，组成的新序列：', li2)

# 列表生成式处理多个参数，如两个列表的情况
a = [1, 2, 3, 4, 5]
b = ["a", "b", "c", "d", "e"]
# 多个参数列表生成式
c = [str(x)+str(y) for x, y in zip(b, a)]
print('多个参数列表生成式：', c)

