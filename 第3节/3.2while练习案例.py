# 求1到100的和

sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1

print("1到100累加的和是：%s" %sum)

# while猜数字,无限机会

import random
num = random.randint(1,100)
count = 0
flag = True
while flag:
    guess_num = int(input("你猜多少？"))
    count += 1

    if guess_num == num:
        flag = False

    else:
        if guess_num > num:
            print("猜大了。")
        else:
            print("猜小了。")

print("你猜对了！！！")
print(f"你总共猜了{count}次。")


