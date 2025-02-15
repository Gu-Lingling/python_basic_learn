# 字典
dict1 = {'小明': 59, '小红':94, '小花':88}
# 空字典
dict2 = {}
dict3 = dict()

print(dict1)
print(dict2)
print(dict3)

# 不能定义重复的字典
# 不能索引
# 用key获取value
print(dict1['小红'])
print(dict1['小花'])

# 字典的嵌套
dict4 = {
         '小唐':{'语文':98 ,'数学':78, '英语':89},
         '小叶':{'语文':83 ,'数学':92, '英语':87},
         '小林':{'语文':88 ,'数学':90, '英语':81},
         '小潘':{'语文':97 ,'数学':99, '英语':99}
        }
print(dict4['小唐']['数学'])
print(dict4['小叶']['英语'])
print(dict4['小林']['语文'])
print(dict4['小潘']['语文'])

# 字典修改
dict5 = {'1':12, '2':9, '3':19, '4':11, '5':13, '6':21}
print(dict5)
dict5['2'] = 14  # 更新
print(dict5)
dict5['7'] = 17  # 新增
print(dict5)

# 删除元素
ele = dict5.pop('7') # 删除元素且得到值
print(dict5)
print(ele)

# 清空字典
dict5.clear()
print(dict5)

# 获取全部key对象
dict5 = {'1':12, '2':9, '3':19, '4':11, '5':13, '6':21}
keys = dict5.keys()
print(f"字典的全部key是；{keys}")

# 遍历字典
for key in keys:
    print(f"字典的key是{key},对应value是{dict5[key]}")
# 方式2 直接循环
for key in dict5:
    print(f"字典的key是{key},对应value是{dict5[key]}")

# 统计字典元素数量
num = len(dict5)
print(num)