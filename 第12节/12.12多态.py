class Animal():
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print('汪汪汪')

class Cat(Animal):
    def speak(self):
        print('喵喵喵')

def make_noise(animal:Animal):
    animal.speak()

dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)

# 接口(抽象类)---都是空的（pass），只用作模板
# 具体功能由具体子类实现
