
"""
count = 0
for i in str1:
    count += 1
print(f"字符串{str1}的长度是：{count}")
"""
str1 = "abcdefg"
str2 = "我不知道啊"

# 定义一个函数，统计字符串的长度
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串:{data}的长度是{count}")

my_len(str1)
my_len(str2)