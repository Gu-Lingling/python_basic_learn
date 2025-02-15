# for语句循环嵌套应用

i = 1
for i in range(1,7):
    print(f"今天是复习第{i}天。")
    for j in range(1,6):
        print(f"已经学习了{j}小时！")
    print("今天可以休息了。")

print(f"这周已学习{i}天，明天可以去考试了！")


# 打印九九乘法表
print("九九乘法表!!!")
for h in range(1,10):
    for l in range(1,h + 1): # 不包含num2，所以要+1
        print(f"{h} * {l} = {h * l}\t",end='')
    print() #仅用作换行输出
