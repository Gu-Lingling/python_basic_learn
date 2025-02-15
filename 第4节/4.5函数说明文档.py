# 通过注释对函数进行说明解释

def add(x,y):
    """
    :param x: # 形参x的说明
    :param y: # 形参y的说明
    :return:  # return返回值的说明
    """
    """
    add函数可以接收两个参数，返回它们的和
    :param x: # x为其中一个加数
    :param y: # y为另一个加数
    :return:  # return返回值是相加的结果
    
    """
    result = x + y
    return result

add(7,4)