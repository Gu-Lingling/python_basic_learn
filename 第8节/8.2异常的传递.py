# 异常的传递性
def func1():
    print("func1开始执行")
    num = 8 / 0
    print("func1结束执行")

def func2():
    print("func2开始执行")
    func1()
    print("func2结束执行")

def main():
    func2()

#main()

# 改
def func3():
    print("func3开始执行")
    num = 8 / 0
    print("func3结束执行")

def func4():
    print("func4开始执行")
    func3()
    print("func4结束执行")

def main1():
    try:
        func4()
    except Exception as e:
        print("出现异常了")
        print(e)

main1()