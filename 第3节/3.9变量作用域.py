# 临时变量作用范围只限定在for循环内部
# 但在外部也可以访问,规则允许，但不规范
# i = 0
for i in range(8):
     print(i)
print(i)