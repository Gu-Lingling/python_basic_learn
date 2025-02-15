class Phone:
    IMET = None
    producer = 'DOG'

    def call_by_4g(self):
        print('使用4G网络')

phone = Phone()
phone.call_by_4g()

# 使用单继承
class Phone2024(Phone):
    face_id = '1000001'

    def call_by_5g(self):
        print("使用5G网络了！！！")

phone = Phone2024()
print(phone.producer)
phone.call_by_5g()

class NFCReader:
    nfc_type = '第五代'
    producer = 'GOD'

    def read_card(self):
        print('NFC读卡')

    def write_card(self):
        print('NFC写卡')

class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print('红外遥控开启了')

# 多继承---父类（子类1，子类2）
class MyPhone(Phone2024, NFCReader, RemoteControl):
    pass

print("---------------------")
my_phone = MyPhone()
my_phone.call_by_4g()
my_phone.call_by_5g()
my_phone.read_card()
my_phone.write_card()
my_phone.control()

# 重名的时候继承的是第一个，按顺序，谁先优先级最高
print(my_phone.producer)
