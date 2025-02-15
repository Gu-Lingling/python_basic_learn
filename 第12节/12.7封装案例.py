class Phone:
    __is_5g_enable = None

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5G开启")
        else:
            print("5G关闭，使用4G网络")

    __is_5g_enable = False

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

phone = Phone()
#phone.is__5g_enable  # 私有的，不能调用
phone.call_by_5g()