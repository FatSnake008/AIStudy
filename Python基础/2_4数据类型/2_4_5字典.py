#以键值对（key:value）形式存储数据的容器
student={
    'name':'小明',
    'age':18,
    'grade':'男',
    'score':[90,85,60]
}

empty_dic={}
print(type(empty_dic))
print(type(student))

student={
    'name':'小明',
    'age':18,

}
print(student['name'])
print(student['age'])
#print(student['height'])
print(student.get('name'))
print(student.get('height'))
print(student.get('height',175))

print("===========================")
#修改、新增
student={
    'name':'小明',
    'age':18
}
student['age']=20
print(student)
student['height']=175
student['hobby']=['篮球','看书']
print(student)
print("===========================")
#删除
student={
    'name':'小明',
    'age':18,
    'grade':'男',
    'score':[90,85,60]
}
del student['grade']
print(student)
#删除并返回值
age=student.pop('age')
print(age)
print(student)

print("===========================")
student={
    'name':'小明',
    'age':18,
    'grade':'男',
}

print(student.keys())
print(student.values())
print(student)
print(student.items())
for key,value in student.items():
    print(f'{key}: {value}')
print(student.clear())

#字典内键必须唯一，键必须不可变（元组可作为键）
print("===========================")
d={'a':1,'a':2,}
print(d)
#a={[1,2]:'test'}
#print(a)
a={(1,2):'test'}
print(a)