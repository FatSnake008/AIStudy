name='小明'
print(type(name))

info="小明说了一句话"
print(type(info))

content='''
第一行
第二行
第三行
'''
print(type(content))

first='Hello'
second=' Python'
print(first+second)
#print(first+2)
print(first+str(2))

print("============================")
#索引
s='Python'
print(s[0])
print(s[3])
print(s[-1])
#切片
ss='Python教程'
print(ss[0:6])
print(ss[:7])
print(ss[6:])

print("============================")
#内置方法
sss='    Hello World    '
#去前后空格
print(sss.strip())
#转小写
print(sss.lower())
#转大写
print(sss.upper())
#替换字符
print(sss.replace('World','Java'))
#统计字符出现次数
print(sss.count('o'))
#判断是否以指定字符开头
print(sss.startswith('Hello'))
print(sss.endswith('World'))

sss=sss.strip()
print(sss.startswith('Hello'))
print(sss.endswith('World'))

print("============================")

name='小红'
scope=98.589
print(f'{name}的成绩是{scope}')
#格式化数字
print(f'成绩保留1位小数{scope:.1f}')

#字符串不能直接修改川内的单个字符
#单引号内不能直接放单引号，需要前加“\”转义，或者直接用双引号
#索引不能越界，长度为6，最大索引5，用s[6]会报错