# 有几个偶数

count = 0
for x in range(1,100):
    if x % 2 == 0:
        count += 1
print(f"这里总共有{count}个偶数！")