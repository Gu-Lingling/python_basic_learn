# 常用功能练习
list = [21, 25, 21, 23, 22, 20]

list.append(31)
print(list)

list_1 = [29, 33, 30]
list.extend(list_1)
print(list)

num_first = list[0]
num_final = list[-1]
print(f"第一个数字是：{num_first}，最后一个数字是{num_final}。")

index = list.index(31)
print(index)

