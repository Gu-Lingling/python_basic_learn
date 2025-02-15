# 字符串三种定义
# 单引号：''  双引号：""  三引号：""" """
name = 'ggb'
print(type(name))
name2 = "gll"
print(type(name2))
name3 = """ggl"""
print(type(name3))

# 单引号内部的双引号只是普通字符而已，反过来也行
print('"abcdefg"')
print("'6666666'")
# 引号的嵌套--转义字符 \
name = " \"hahaha\"\"\"  "
print(name)

# 字符串拼接
star = "herherher"
print("she " + star + 's')
pheno = "eight"
print("我的电话是" + pheno)

# 字符串格式化
address = '123456123'
address2 = 123789123 #将数字转换成了字符串
message = "请call %s,或者 %s" % (address, address2)
print(message)
place = "宇宙"
location = "这里是%s" % place
print(location)

# %d，将内容转化为整数
# %f，将内容转换成浮点型
# %s，将内容转换成字符串
fgh=18.863
fffff = "我现在有%d元" % fgh
print(fffff)

# 格式化的精度控制
birth = 2003
time = 9.344872488978
T = "100米用时：%7.4f s" % time
print(T)

# 快速格式化
ex = "哈哈哈"
kk = 1793
keke = 4691
# f:format格式化
print(f"我想说{ex}, 你有{kk},  我有{keke}")

# 对表达式进行格式化
print("5*4的结果为:%f" %(5 * 4) )
print(f"3的5次方为：{4**4}")