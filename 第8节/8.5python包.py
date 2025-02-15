"""
import my_package.module1
import my_package.module2

my_package.module1.info_print1()
my_package.module2.info_print2()
"""

from my_package import module1
from my_package import module2
# 这样就不用写包名
module1.info_print1()
module2.info_print2()

# 还可以这样
from my_package.module1 import info_print1
info_print1()