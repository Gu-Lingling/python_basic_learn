# 发奖金
bonus = 54554

for i in range(1,21):
    import random
    level = random.randint(1,10)

    if level < 5:
        print(f"员工{i}绩效分为{level}，条件不满足，没有奖金")
        continue

    if bonus >= 5000:
        bonus -= 5000
        print(f"员工{i}绩效分为{level},满足条件，发放奖金5000，总奖金还剩{bonus}元")
    else:
        print(f"余额不足，当前余额{bonus}元，剩下{21-i}个员工下个月再补回。")
        break