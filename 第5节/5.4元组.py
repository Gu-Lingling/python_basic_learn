# 元组，定义完成后，不能被篡改。只读

t1 = (1, 'sss', True)
t2 = ()
t3 = tuple()
print(f"t1的类型是{type(t1)}")
print(f"t2的类型是{type(t2)}")
print(f"t3的类型是{type(t3)}")

# 单个元素的元组
t4 = ('aaa',) #要写单独逗号
print(f"t4的类型是{type(t4)}")

# 元组的嵌套
t5 = ((1, 2, 3),(4, 5, 6))
print(f"t5的类型是{type(t5)}")
print(t5)

# 索引引出内容
num = t5[1][2]
num2 = t5[0][1]
print(num)
print(num2)

# 元组的操作
t6 = (33, 77, 99, 55, 88)
index = t6.index(55)  # 查找元素在元组中的下标
print(index)

t7 = (33, 77, 99, 88, 88, 99, 999, 99, 9, 99)
num = t7.count(99) # 统计特定元素的数量
print(num)

t8 = (33, 77, 88, 88, 99, 999, 99)
total = len(t8)  # 元组共有多少元素
print(total)

# 元组的遍历
# while循环
index= 0
while index < len(t8):
    print(f"元组的元素有{t8[index]}")
    index += 1

# for循环
for element in t6:
    print(f"元组的元素有{element}")

# 修改元组会报错，元组不可修改
# t6[2] = 45

# 但元组里嵌套的list可以修改
t9 = (1, 2, [45, 48, 51, 54])
print(t9)
t9[2][2] = 50
print(t9)