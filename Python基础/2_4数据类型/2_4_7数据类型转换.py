#把一种数据类型转换成另一种类型，有自动转换和强制转换
'''
input_age=input("请输入年龄")
age=int(input_age)
print(age+2)
'''
score=96
print('你的成绩是'+str(score))

price=float('29.9')
print(price*2)

print("=========================")
lst=[1,2,3]
t=tuple(lst)
print(t)

t=[4,5,6]
lst=list(t)
lst[0]=10
print(lst)

lst=[4,5,5,6]
s=set(lst)
print(s)

print("=========================")
# print(bool(0))
# print(bool(5))
# print(bool(0.0))
# print(bool(3.14))
# print(bool(""))
# print(bool("abc"))
# print(bool([]))
# print(bool([1]))
# print(bool({}))

#s='abc'
#print(int(s))
s=input('请输入转换数字')
if s.isdigit():
    num=int(s)
    print(num)
else:
    print('s不是有效数字')

print("=========================")
print(5+3.14)
print(True+2)
print(False+3)