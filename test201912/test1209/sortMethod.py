
# ===list对象的方法sort排序 (直接排序，不生成一个新序列，原序列改变) ===


# 情况一：list对象为数字
li = [2, -4, 33, 21, 6, 94, 20, 46, 0, 29, -34, 8]

# sort()默认排序从小到大
li.sort()
print("从小到大排序：", li)

# reverse = Trur 排序从大到小
li.sort(reverse=True)
print("从大到小排序：", li)

# 情况二：list对象为字符串
li1 = ['abc', 'abcdef', 'abcde', 'a', 'abcdefghijk']
li1.sort(key=lambda x: len(x), reverse=True)
print("字符串 从长到短排序：", li1)

# 情况三：list对象为元祖
li2 = [('a', 2), ('b', 90), ('c', 28), ('d', -3)]
li2.sort(key=lambda x: x[1])
print("元祖 第二个数从小到大排序：", li2)

# 情况四：list对象为字典
li3 = [{'a': 2}, {'b': 90}, {'c': 28}, {'d': -3}]
li3.sort(key=lambda x: list(x.values())[0])
print("字典 第二个数从小到大排序：", li3)


# ===python内置函数sorted (排序后生成一个新序列，原序列不变) ===

# 对序列进行排序
list = [2, -4, 33, 21, 6, 94, 20, 46, 0, 29, -34, 8]
a = sorted(list)
print("默认排序，从小到大：", a)
b = sorted(list, reverse=True)
print("降序排列，从大到小", b)

#对字符串进行排序
s = 'hello world'
s1 = sorted(s)
print('原字符串：', s)
print('排序后的：', s1)

#对元祖进行排序
tup = (3, 9, 33, 1, 90, 2, -59, 59)
tup1 = sorted(tup)
print('原元祖：', tup)
print('排序后，默认升序，元祖', tup1)

#对字典进行排序
dic = {'a': 3, 'b': 9, 'c': 33, 'd': 1, 'f': 90, 'g': 2, 'h': -59, 'i': 59}
dic1 = sorted(dic.items(), key=lambda x: x[1])
print('原字典：', dic)
print('根据value升序排序的字典：', dic1)
