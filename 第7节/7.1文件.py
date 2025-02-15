# 打开文件
# f是文件对象
f = open("D:/Python.code/file/桃花庵歌.txt","r",encoding="UTF-8")
print(type(f))

# 读取
#print(f.read(8))  # 指针存在于最后一个字符那里，再读就从这开始

#lines = f.readlines() # 读取全部行，封装到列表中
#print(lines)
#print(type(lines))

# readline() 一次读一行
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(line1)
print(line2)
print(line3)

# for循环读取行
for line in f:  #受上面三行影响，这个for从第四行读取
    print(line)

# 文件的关闭 解除对文件的占用
f.close()

print("----------------------")

# with open as...语句 执行完后会自动关闭文件
with open("D:/Python.code/file/桃花庵歌.txt","r",encoding="UTF-8")as f:
    for line in f:
        print(line)
