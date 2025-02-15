# 有几个a
from itertools import count

sentence = "life is struggle"
count = 0

for x in sentence:
    if x == 'e':
        count += 1

print(f"有{count}个字母e")
