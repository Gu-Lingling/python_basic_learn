# 终极猜数字

import random
num = random.randint(1,10)

guess_num = int(input("请输入你要猜测的数字："))

if guess_num == num:
    print("你第一次就猜中了！！！")
else:
    if guess_num > num:
        print("猜大了。")
    else:
        print("猜小了。")

    guess_num = int(input("第二次机会，再猜吧："))

    if guess_num == num:
        print("这一次猜中了！！！")
    else:
        if guess_num > num:
            print("猜大了。")
        else:
            print("猜小了。")

        guess_num = int(input("珍惜最后一次机会："))

        if guess_num == num:
            print("最后一次猜中了！！！")

        else:
            print("时运不系于你啊...")
print(f"真实数字是{num}。")
