# 函数参数的使用
def add(x,y,z):
    result = x + y + z
    print(f"{x} + {y} + {z}= {x + y + z}")

# add(5,6,7)
# add(54545,45454,0)

# 检测体温
def tem(t):
    if t < 37.5:
        print("你体温正常。")
    else:
        print("你发烧了，请注意身体。")

tem(36.5)
tem(38.7)