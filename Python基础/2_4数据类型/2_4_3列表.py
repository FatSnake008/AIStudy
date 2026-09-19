#字符串不可变，列表可变
empty_list=[]
print(empty_list)
nums=[1,2,3,4,5]
print(nums)
mix_list=[18,'小明',1.75,True]
print(mix_list)
print(type(mix_list))
#索引取值
fruits=['apple','banana','orange']
print(fruits[0])
print(fruits[1])
print(fruits[-1])
#切片包含开始，不包含结束，省略索引可取到结束
nums=[1,2,3,4,5]
print(nums[1:3])
print(nums[:3])
print(nums[2:])

print("=================================")
fruits=['apple','banana','orange']
fruits[1]="香蕉"
print(fruits)

print("=================================")
fruits=['apple','banana','orange']
#添加元素在最后
fruits.append('pear')
print(fruits)
#在指定位置插入元素
fruits.insert(1,'peach')
print(fruits)
#移除指定元素
fruits.remove('banana')
print(fruits)
#删除元素
del fruits[0]
print(fruits)
#删除最后一个元素并返回
fruits.pop()
print(fruits)

print("=================================")
#升序排序
nums=[3,2,1,5,4]
nums.sort()
print(nums)
#反转列表
nums.reverse()
print(nums)

print(nums.count(3))
print(len(nums))

#列表索引不可越界
#remove()删除不存在的元素会报错，可先进行if判断

print("=================================")
l1=[1,2,3]
l2=l1
print(l1)
print(l2)
l2.remove(1)
print(l1)
print(l2)
#列表是可变对象，赋值是引用不是赋值，修改其中一个另一个也修改
