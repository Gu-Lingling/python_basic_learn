word = "life is struggle"

# 通过下标索引取值
value1 = word[0]
print(value1)
value2 = word[-4]
print(value2)

# 字符串不能修改
#word[3] = 'u'

# 查找索引值
value3 = word.index("is")
print(f"起始下标是：{value3}")\

# 字符串替换
word2 = word.replace("struggle", "meaningful" )
print(word)
print(word2)

# 字符串分割，返回一个列表
word3 = word.split(" ") # 里面填分割的字符，依靠其分割
print(word3,type(word3))

# 字符串的规整操作
word = "    life  is     struggle  "
word4 = word.strip() # 不传入参数，作用是去除首尾空格
print(word4)

word = "123life  is     struggle321"
word5 = word.strip("123") # 里面的字符都会被去除，
print(word5)

# 统计某字符出现的次数
word = "Shall we talk Shall we talk"
count = word.count("l")
print(count)

# 统计字符串的长度
length = len(word)
print(length)