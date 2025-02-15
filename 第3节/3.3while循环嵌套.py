# while循环嵌套应用

day = 1
while day <= 6:
    print(f"今天是第{day}天，开始学习。")

    hour = 1
    while hour <= 5:
        print(f"才学了{hour}小时，继续学吧。")
        hour += 1

    print("今天学够了,休整。")
    day += 1

print("你学够六天了，可以去考试了。")