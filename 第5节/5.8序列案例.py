# 练习 取出love  糟糕。

word = "djdds  .evol  dasdud, kve"

word1 = word[::-1]
print(word1)

word2 = word1[8:18:1]
print(word2)

word3 = word2.split(" ")
print(word3)

word4 = word3[2].replace(".", " ")
print(word4)
