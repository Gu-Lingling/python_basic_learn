# 函数作为参数传递
def test_func(compute):
    result = compute(7,17) #compute()是函数
    print(type(compute))
    print(result)

def compute(x,y):
    return x*y

def compute1(x,y):
    return x+y

test_func(compute)
test_func(compute1)