# 关键字参数， 键=值
# 可以不按固定顺序
# 可以和位置参数混用，但位置参数要在前
def user_info(name,age,gender):
    print(f"姓名是{name}，年龄是{age}，性别是{gender}。")

user_info(20,'女','小红') #位置乱了
user_info(age=18,gender='女',name='洛落')  # 可以乱序
user_info('未雅',gender='女',age=16) # 有位置参数，要放最前

#设置默认值必须在最后
def user_info1(name,age,gender='女'):
    print(f"姓名是{name}，年龄是{age}，性别是{gender}。")

user_info1('白',24)
user_info1('古',22,'女')

# 不定长参数
def user_info2(*args):
    print(type(args))
    print(args)

user_info2(1,8,'q')
user_info2(9,'p')

def user_info3(**kwargs):
    print(type(kwargs))
    print(kwargs)

user_info3(a='111', b=753, c='uio')

