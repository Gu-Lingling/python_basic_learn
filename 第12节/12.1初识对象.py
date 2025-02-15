# 设计类，创建对象，对象属性赋值
class Student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None

stu_1 = Student()
stu_1.name = '青竹'
stu_1.gender = '女'
stu_1.nationality = '中国'
stu_1.native_place = '韶关'
stu_1.age = 18

print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.native_place)
print(stu_1.age)
print(stu_1)
