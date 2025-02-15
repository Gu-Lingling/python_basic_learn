# 读取字出现的次数

poem = open("D:/Python.code/file/桃花庵歌.txt","r",encoding="UTF-8")

# 方式一
content = poem.read()
count = content.count("酒")
print(content)
print(count)

poem.close()