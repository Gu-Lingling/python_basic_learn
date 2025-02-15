# 私有成员变量和成员方法， __两个下划线开头意味着私有
class Phone:
    __current_voltage = None # 私有的了

    def __keep_single_core(self):   # 私有的方法
        print("让CPU以单核模式运行")

    __current_voltage = 1.1

    # 使用公开的方法可以调用私有的变量和方法
    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("开启")
        else:
            self.__keep_single_core()
            print("无法开启，设置省电")


phone = Phone()
# phone.__keep_single_core()  # 不能用了
#phone.__current_voltage
#print(phone.__current_voltage)

# 通过调用公开的方法来访问内部私有的方法和变量
# 私有的只能内部自己使用
phone.call_by_5g()