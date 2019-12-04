
# 定义列表
list = [1, 3, 71, 25, 31, 6, 7, 15]

# 冒泡排序实现
for j in range(len(list)-1):
    for i in range(len(list)-1-j):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
print(list)

# python中冒泡排序函数sort
# list.sort()
# print(list)
