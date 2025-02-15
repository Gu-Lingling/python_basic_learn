class Phone:
    IMEI = None
    producer = 'HHH'

    def call_by_5g(self):
        print('父类5G')

# 复写父类的内容
class My_phone(Phone):
    producer = 'HDD'  # 复写父类的内容

    def call_by_5g(self):# 复写父类的内容
        print('子类5G')
        # 调用父类
        print(Phone.producer) # 调用父类成员
        print(Phone.call_by_5g(self)) # 调用父类方法
        # 另一种方法
        print(super().producer) # 调用父类成员
        print(super().call_by_5g())

phone = My_phone()
print(phone.call_by_5g())
print(phone.producer)
