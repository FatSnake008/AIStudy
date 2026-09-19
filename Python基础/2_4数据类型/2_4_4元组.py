#存储多个数据的容器，不可变
#定义普通元素
fruits=('apple','banana','orange')

empty_tuple=()
single_tuple=(18,)
wrong_tuple=(1)
print(type(fruits))
print(type(empty_tuple))
print(type(single_tuple))
print(type(wrong_tuple))

print("=====================================")
nums=(10,20,30,40)
print(nums[0])
print(nums[-1])
#切片都是省略最后的
print(nums[1:3])
print(nums[:3])
print(nums[3:])

print("=====================================")
fruits=('apple','banana','orange')
#fruits[0]="banana"
#del fruits[1]
#元组不可添加、删除、修改

#元组常见操作
a=(1,2,3)
b=(4,5,6)
print(a)
print(b)
print(a+b)
print(a*2)
print(len(a))
print(a.count(2))
print(a.index(3))

info=('小明',18,'男')
name,age,gender=info
print(name)
print(age)
print(gender)

#单个元素元组必须加逗号
#元组不可变是“元素本身不可替换”，但是元素如果是可变类型（列表），列表内部可替换
tuple_list=(1,2,3,[4,5,6])
print(tuple_list)
tuple_list[3][0]=999
print(tuple_list)