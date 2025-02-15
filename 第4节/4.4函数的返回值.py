def mul(a,b):
    result = a * b
    return result
    print("abcdefg") # return后函数内部的代码不执行了


# result返回给了变量r
r = mul(13,21)
print(r)

# None类型
def greet1():
    print("晚上好！")


result1 = greet1()
print(f"无返回值函数，返回的内容是：{result1}")
print(f"无返回值函数，返回的类型是：{type(result1)}")

# 主动返回None
def greet2():
    print("晚上真好！")
    return None

result2 = greet2()
print(f"无返回值函数，返回的内容是：{result2}")
print(f"无返回值函数，返回的类型是：{type(result2)}")

# None用于if判断
def check_age(age):
    if age >18:
        return "SUCCESS"
    else:
        return None

age_result = check_age(13)
if not age_result:
    print("未成年")

# 让变量存储无意义的None
name = None
print(name)