# 猜数字

num = 18

if int(input("请猜测一个数字：")) == num:
    print("你第一次就猜对！！！")
elif int(input("猜错了，还有两次机会，再猜一次：")) == num:
    print("第二次就猜对了！！！")
elif int(input("又猜错了，最后一次机会，猜吧：")) == num:
    print("最后一次对了！！！")
else:
    print("你是猪吗？")

