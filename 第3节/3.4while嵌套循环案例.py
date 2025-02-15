# print后+end='',可以不换行输出
# \t符号等同于键盘上的tab键，可以让多行字符串对齐
# 打印九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{i} * {j} = {i * j}\t",end='')
        j += 1
    i += 1
    print()   #空内容，仅输出一个换行
