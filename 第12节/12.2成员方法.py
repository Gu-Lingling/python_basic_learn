# 成员方法其实就是写在类内部的函数，称为方法
class Student:
    name = None

    def say_hi(self):
        print(f'大家好，我是{self.name}。')  # 要加self才能访问成员变量

    def say_hi2(self,msg):
        print(f"大家好，我是{self.name},{msg}")


stu = Student()
stu.name = '青檀'
stu.say_hi()
stu.say_hi2("你们好啊")


stu2 = Student()
stu2.name = '青竹'
stu2.say_hi()
stu2.say_hi2("你们好呀")
