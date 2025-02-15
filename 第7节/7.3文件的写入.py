# 文件的读写
poem = open("D:/Python.code/file/poem.txt","w",encoding="UTF-8")
# 文件不存在的话，要写东西时会自动创建一个文档，
# 存在的话就会清空再写
poem.write("醉后不知天在水") # 写入了缓存区，还没在硬盘内存里

poem.flush() # 内容刷新，这时才真正写到硬盘里

poem.close() # 内置了flush的功能