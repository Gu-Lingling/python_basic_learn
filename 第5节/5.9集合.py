# 定义集合--不重复且无序
set1 = {1, 6, 'hehe', True, True, 1, 8}
# 空集合
set2 = set()

print(set1)
print(set2)
print(type(set2))

# 添加新元素
set1.add("haha")
print(set1)
set2.add(888)
print(set2)

# 移除元素
set1.remove(6)
print(set1)
set2.remove(888)
print(set2)

# 随机取元素
set3 = set1.pop() # 无参数，随机的
print(set3)

# 清空
set4 = {'2', 'a', 'o', '8'}
set4.clear()
print(set4)

# 取两个集合的差集
set5 = {1,2,3,4,5}
set6 = {4,5,6,7,8}
set7 = set5.difference(set6)
set8 = set6.difference(set5)
print(set5)
print(set6)
print(set7)
print(set8)

# 消除相同的元素
set5 = {0,2,3,4,5,6}
set6 = {4,5,6,7,8}

set5.difference_update(set6)
print(set5)
print(set6)

# 合并,不会修改已有集合，而是获得一个新集合
set9 = {1,2,3,4,5,6}
set10 = {4,5,6,7,8,9,10}
set11 = set9.union(set10)
print(set11)

# 统计集合元素
set12 = {1,2,3,4,5,6,5,5,6,8,1}
num = len(set10)
print(num)
num1 = len(set12)  # 会去重
print(num1)

# 集合的遍历,不能索引不能用while，但可以用for
for element in set12:
    print(f"集合的元素有：{element}")