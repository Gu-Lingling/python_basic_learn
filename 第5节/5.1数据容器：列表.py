# 列表的定义语法
list1 = ['haha', 'hehe', 'xixi']
print(list1)
print(type(list1))

list2 = ['hhh', 777, True]
print(list2)
print(type(list2))

list3 = [[1,2,3], ['H', 'I', 'J'], [True, False]]
print(list3)
print(type(list3))

# 列表的下标索引,取对应数字
list4 = [32, 56, 78, 19, 84, 44, 65, 8, 99, 23]
print(list4[0])
print(list4[3])
print(list4[9])
print(list4[-1])
print(list4[-10])
print(list4[-3])

# 嵌套的列表元素取法
list5 = list3
print(list5[0][2])
print(list5[2][1])
print(list5[1][0])

# 列表的方法
# 1.查询
list6 = ['H','I','J','K','L','M','N']
index = list6.index('K')    # 关键语法
print(f"索引值是:{index}")

# 2.修改特定位置下标索引的值
list7 = [33, 22, 11, 44, 77, 55]
print(list7[3])
list7[3] = 666  # 关键语法
print(list7[3])

# 3.元素插入
list7.insert(2,999)  # 关键语法
print(list7)

# 4.元素追加，写一个到尾部
list7.append(888)   # 关键语法
print(list7)

# 5.另一种，追加一整个新的数据容器到尾部
list8 = [111, 222, 333]
list7.extend(list8)  # 关键语法
print(list7)

# 6.删除指定的元素
del list7[5]  # 关键语法
print(list7)

element = list7.pop(3)
print(list7)  # 另一种语法,把删掉的元素作为了返回值
print(f"取出的元素是{element}")

# 7.删除某元素在列表的第一个匹配项
list7.insert(1,22) #先插入一个元素
list7.insert(2,22) #再插入一个元素
print(list7)
list7.remove(22) # 关键语法
print(list7)
list7.remove(22) # 再移除一个，被移除的是第一个
print(list7)
list7.remove(22) # 再再移除一个，被移除的是第一个
print(list7)

# 8.清空列表
list7.clear() #关键语法
print(list7)

# 9.统计某元素在列表中的数量
list7 = [33, 999, 996, 999, 99, 666, 999, 888, 111, 222, 333]
print(list7)
count = list7.count(999)  # 关键语法
print(f"999数字有{count}个")

# 10. 统计列表里元素数量
num = len(list7)  #len()函数
print(f"列表的元素数量有；{num}个")
