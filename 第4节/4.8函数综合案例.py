money = 5000000
name = None
name = input("请输入您的姓名：")

def query(show_header):
    if show_header:
        print("---查询余额---")
    print(f"{name},你好，你的余额为：{money}元。")

def saving(num):
    global money
    money += num
    print("---存款---")
    print(f"你好，你存款{num}元成功。")
    query(False)

def get_money(num):
    global money
    money -= num
    print("---取款---")
    print(f"你好，你取款{num}元成功。")
    query(False)

def main():
    print("-----主菜单-----")
    print("你好，请选择操作：")
    print("查询余额\t【输入1】")
    print("存款\t\t【输入2】")
    print("取款\t\t【输入3】")
    print("退出\t\t【输入4】")
    return input("请输入你的选择：")

while True:
    keyboard_input = main()
    if keyboard_input == '1':
        query(True)
        continue # 继续下一次循环，回到主菜单
    elif keyboard_input == '2':
        num = int(input("你要存多少钱？请输入："))
        saving(num)
        continue
    elif keyboard_input == '3':
        num = int(input("你要取多少钱？请输入："))
        get_money(num)
        continue
    else:
        print("下次一定！")
        break