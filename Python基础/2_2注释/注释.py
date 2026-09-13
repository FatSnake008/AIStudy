print('Hello World') #单行注释
#print('你好')  # 临时屏蔽代码

'''
多行注释
一
二
三

'''

"""
这个也是多行注释

"""

def add(a,b):
    """
    功能：计算两值的和
    :param a: 第一个加数
    :param b: 第二个加数
    :return: a+b的结果
    """
    return a+b

help(add)