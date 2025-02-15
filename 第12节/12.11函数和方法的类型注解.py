from typing import Union

# 对形式参数进行注解
def add(x:int,y:int):
    return x + y

add(5,8)

# 对返回值进行注解
def func(data:list) -> list:
    return data

#func(1)   #也不会报错，因为不是强制性的
func([])

# Union类型进行联合类型注解
my_list: list[Union[int, str]] = [1, 3, 'wdw', 'jjg'] # Union语法

# 传入或返回哪一种都行
def func(data:Union[int,float]) -> Union[int,str]:
    pass

func(12)
