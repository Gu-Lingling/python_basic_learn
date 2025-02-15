import random
import json

# 各种类型注解
var1: int = 100
var2: float = 3.14
var3: bool = False
var4: str = 'ASD'

# 写错了也不会报错
var: int = 'hahaha'

class Teacher:
    pass
tea: Teacher = Teacher()

list1: list = [1, 5, 9]
tuple1: tuple = (1, 3, 5)
dict1: dict = {'G':888}
set1: set = {1,'1',1.0}
str1: str = '何以解忧，唯有杜康'

list2: list[int] = [1, 5, 9]
tuple2: tuple[int,int,int] = (1, 3, 5) # tuple要全部标出来
dict2: dict[str,int] = {'G':888}
set2: set[int|str|float|bool] = {1,'1',1.0,True}
str2: str = '何以解忧，唯有杜康'

data = 'str'

# 另一种写法，在注释中进行类型注解
var5 = random.randint(1,10)      # type:int
var6 = json.loads('{"uuu":"www"}')    # type:dict

def func():
    pass

var7 = func()                         # type:int

