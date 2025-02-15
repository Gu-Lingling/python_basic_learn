# 局部变量,出了函数就不能使用了
def test_a():
    number = 10
    print(number)

test_a()
# print(number)

# 全局变量
num = 17
def test_b():
    print(num)

def test_c():
    print(num)

test_b()
test_c()

# global关键字
num2 = 101
def test_d():
    print(num2)

def test_e():
    global num2 # 把它变成全局变量了
    num2 = 100
    print(num2)

test_d()
test_e()
print(num2)