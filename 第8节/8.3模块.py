# 导入time模块使用sleep功能
"""
import time

print("怎么了")
time.sleep(3)  # 暂停几秒钟，sleep()是time里定义的函数
print("你累了")
"""

# 只导入具体功能使用
"""
from time import sleep

print("怎么了")
sleep(3)  # 直接用sleep函数
print("还好吗")
"""

# 导入全部功能,但只需写函数，不用写time.
"""
from time import*

print("怎么了")
sleep(3)  # 直接用sleep函数
print("为什么")
"""

# 模块定义别名
import time as t
print("怎么了")
t.sleep(4)  # 直接用sleep函数
print("那就好")

# 也可以：from time import sleep as (别名)

