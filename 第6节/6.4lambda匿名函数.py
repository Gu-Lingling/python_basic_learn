# lambda匿名函数只能用一次，但简单，只需要一行代码
def test_func(compute):
    result = compute(6,3) #compute()是函数
    print(type(compute))
    print(result)

lambda x, y: x + y  #整个放进去

test_func(lambda x, y: x + y) #直接写也行
test_func(lambda x, y: x ** y)