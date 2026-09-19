#存储不重复、无序元素的容器
#元素唯一，自动去重
#元素是不可变的，集合可变可增删元素
nums={1,2,3,3,3}
print(nums)

empty_set=set()
print(empty_set)
wrong_empty_set={}
print(wrong_empty_set)

list1=[1,2,2,3]
print(list1)
s=set(list1)
print(s)
print(type(nums))
print(type(empty_set))
print(type(wrong_empty_set))
print(type(s))

print("======================================")
fruits={'apple','banana','orange'}
print('banana' in fruits)
print('peach' in fruits)

print("======================================")
fruits={'apple','banana','orange'}
fruits.add('peach')
print(fruits)
#元素位置随机，添加也随机
fruits.update(['grape','mango'])
print(fruits)
fruits.remove('grape')
print(fruits)
fruits.discard('watermalon')
print(fruits)
#remove删除不存在的报错，discard删除不存在的不报错
fruit=fruits.pop()
print(fruits)

fruits.clear()
print(fruits)

print("======================================")
a={1,2,3,4,5,6}
b={3,4,5,6,7,8}
#并集
print(a | b)
print(a.union(b))
#交集
print(a&b)
print(a.intersection(b))
#差集
print(a-b)
print(a.difference(b))
print(b-a)
print(b.difference(a))
print("======================================")
#集合无序，不能用索引取值
a={1,2,3,4,5,6}
#print(a[0])
#集合元素必须不可变，列表、字典不能作为集合元素
#b={[1,2,3],4}
#print(b)
b={(1,2,3),4}
print(b)