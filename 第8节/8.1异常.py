#file = open("D:/test.txt","r",encoding="UTF-8")

#异常处理程序
try: # 表示这里可能出现异常
    file = open("D:/test.txt","r",encoding="UTF-8")
except:
    # 如果报错就用w模式打开
    file = open("D:/test.txt","w",encoding="UTF-8")

# 捕获指定的异常
try:
    print(name)
except NameError as e: # 只能捕获NameError的异常
    print("出现了变量未定义的异常")
    print(e)

# 捕获多个异常
try:
    1 / 0
    #print(name)
except(NameError, ZeroDivisionError) as e:
    print("出现了异常")
    print(e)

# 捕获所有异常
try:
    1 / 0
    print(gender)
except Exception as e: # 可以捕获全部异常
    print("出现异常了")

# else   finally
try:
    file1 = open("D:/test556.txt","r",encoding="UTF-8")
except Exception as e:
    file1 = open("D:/test556.txt","w",encoding="UTF-8")
    print("有异常，打开它")
else:    # 没有异常的话也会执行它
    print("没有异常")
finally:     # 不管有无异常，最后都会执行
    print("我一定会执行")
    file1.close()