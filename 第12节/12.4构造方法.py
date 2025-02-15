class Student:
    # name = None
    # age = None
    # tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print('创建了一个Student类的对象')

stu1 = Student('小人',18,'123456789')
print(stu1)  # 会打印内存地址
print(stu1.name)
print(stu1.age)
print(stu1.tel)

