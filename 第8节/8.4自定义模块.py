# 自定义模块
import my_module
# 或者
from my_module import add
# from my_module2 import add

add(2,8)

# __all__变量

from my_module1 import*
# test_a(1,3)  #用了all变量，不能执行了

test_b(1,3)
