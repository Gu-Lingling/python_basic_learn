# 序列的切片

list = [0, 1, 2, 3, 4, 5, 6]
list2 = list[0:5:2]
print(list2)

tuple = (0, 1, 2, 3, 4, 5, 6)
tuple1 = tuple[:]
print(tuple1)

str = "0123456789"
str1 = str[::3]
print(str1)

str2 = str[::-1]  # 从后向前取
print(str2)

str3 = str[5:1:-2]   # 不包含1本身(终点)
print(str3)
str4 = str[7:0:-1]
print(str4)

tuple = (0, 1, 2, 3, 4, 5, 6)
tuple2 = tuple[::-2]
print(tuple2)