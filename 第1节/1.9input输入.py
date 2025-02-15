# input()语句
print("请告诉我你是谁？")
name = input()
print("我知道，你是：%s" % name)

# 提示语句可以放在input里

name = input("你是？")
print("你是：%s" % name)

# 写入的数据会变成字符串
print(type(name))
name = int(name)
print(type(name))