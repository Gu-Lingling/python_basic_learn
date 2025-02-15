# if语句的嵌套
# case1
"""
if int(input("你的身高是？")) > 120:
    print("超出限制，禁止。")
    print("若是高级VIP，则可准许")

    if int(input("你的VIP级别是？")) > 3:
        print("你是高级VIP，可以进入游玩。")
    else:
        print("不好意思，您没资格。")
else:
    print("欢迎小朋友免费进来玩")
"""

# case2
age = 19
year = 13
level = 7

if age >= 18:
    print("你已成年")
    if age < 50:
        print("你的年龄合格。")
        if year > 10:
            print("恭喜你，年龄和经验要求达标，可以获得补贴。")
        elif level > 5:
            print("年龄和级别要求达标，可以获得补贴。")
        else:
            print("很可惜，你经验与级别都不达标。")
    else:
        print("你的年龄过大，不合适。")

else:
    print("你还小，还得沉淀。")