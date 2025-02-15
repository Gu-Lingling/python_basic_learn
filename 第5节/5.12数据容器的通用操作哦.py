list0 = [1,2,3,4,5]
tuple0 = (1,2,3,4,5)
str0 = 'abcdefg'
set0 = {1,1,2,3,3,4,5,6,5}
dict0 = {"key1":1,"key2":2,"key3":3,"key4":5,"key5":4}
print(len(list0))
print(len(tuple0))
print(len(str0))
print(len(set0))
print(len(dict0))

print(max(list0))
print(max(tuple0))
print(max(str0))
print(max(set0))
print(max(dict0))

print(min(list0))
print(min(tuple0))
print(min(str0))
print(min(set0))
print(min(dict0))

# 转换功能
print(list(list0))
print(list(str0))
print(tuple(str0))
print(tuple(dict0))
print(str(list0)) # 已经是字符串了
print(str(dict0))
print(str(set0))
print(set(list0))
print(set(str0))
print(set(dict0))  # value丢失，key保留

# 排序功能  排序的结果会变成列表
list1 = [33,54,64,12,2,8,79,91,45,53]
tuple1 = [33,54,64,12,2,8,79,91,45,53]
print(sorted(list1))
print(sorted(tuple1))
print(sorted(list1,reverse=True))
print(sorted(tuple1,reverse=True))

# 字符串比大小--每个字符一位位的比较
print('abce' > 'abcdefg')
print('a' < 'A')

# ke1与key2
print('key1' < 'key2')