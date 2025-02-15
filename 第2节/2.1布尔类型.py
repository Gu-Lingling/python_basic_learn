# 演示布尔类型

# 定义变量存储布尔类型的数据
bool_1 = True
bool_2 = False

print(f"bool_1变量的内容是：{bool_1}, 类型是：{type(bool_1)}")
print(f"bool_2变量的内容是：{bool_2}, 类型是：{type(bool_2)}")

# 比较运算符的使用
# == != > < >= <=
num1 = 10
num2 = 10
print(f"10 == 10 的结果是：{num1 == num2}")

num3 = 10
num4 = 9
print(f"10 != 9 的结果是：{num3 != num4}")

str1 = "abc"
str2 = "bca"
print(f"abc == bca的结果是:{str1 == str2}" )
print(f"abc != bca的结果是:{str1 != str2}" )

num5 = 12
num6 = 13
print(f"12 > 13的结果是：{num5 > num6}")
print(f"12 < 13的结果是：{num5 < num6}")

num7 = 7
num8 = 7
print(f"7 <= 7的结果是：{num7 <= num8}")