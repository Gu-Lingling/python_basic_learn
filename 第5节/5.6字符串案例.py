word = "shall we talk shall we dance"

count = word.count("a")
print(f"字符串中有{count}个a字符")

word2 = word.replace(" ","|")
print(word2)

word3 = word2.split("|") # 分割后得到列表
print(word3)