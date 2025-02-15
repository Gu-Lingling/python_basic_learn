# if,elif,else多条件判断语句

"""
height = int(input("请输入你的身高："))
vip_level = int(input("请输入你的会员等级："))
day = int(input("今天日期是几号："))

if height < 120:
    print("身高小于一米二，可以免费进入。")
elif vip_level >= 3:
    print("您是高级vip成员，可以进入。")
elif day == 10:
    print("今天10号，可以进入。")
# else也可以不写
else:
    print("不满足条件，你不能参加。")
"""

# input语句可以直接写在if，elif里
if int(input("请输入你的身高：")) < 120:
    print("身高小于一米二，可以免费进入。")
elif int(input("请输入你的会员等级：")) >= 3:
    print("您是高级vip成员，可以进入。")
elif int(input("今天日期是几号：")) == 10:
    print("今天10号，可以进入。")
else:
    print("不满足条件，你不能参加。")