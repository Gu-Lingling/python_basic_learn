class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student类对象，name:{self.name}，age:{self.age}"

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age

stu1 = Student('小好人',28)
print(stu1)
print(str(stu1))

stu2 = Student('很好人',28)
stu3 = Student('老好人',46)
print(stu2 < stu3)
print(stu2 > stu3)
print(stu2 <= stu3)
print(stu2 >= stu3)
# 若没有__eq__定义，则也可以比较相等
# 但比较的是它们的内存地址，结果永远是False
# 因为内存不会一样
print(stu2 == stu3)
print(stu1 == stu2)