hairs = ['brown','blond','red']
eyes = ['brown','biue','green']
weights = [1,2,3,4]


the_count = [1,2,3,4,5]
fruits = ['苹果','橘子','梨','杏']
change = [1,'一美分',2,'10美分',3,'25美分']

#第一种循环方式是通过列表
for number in the_count:
    print ("这是数字%d" %number)

#当然我们的列表也可以是混合的
#我们需要注意当我们不知道列表中有什么时，我们应该使用%r

for i in change:
    print ("I got %r" %i)

#我们也可以在一个空列表中创建一个列表
element = []

#然后使用范围函数从0到5计数
for i in range(0,6):
    print ("添加%d到列表(list)中。" %i)
    #append是一个能将变量添加到列表(list)中的函数
    element.append(i)


#然后我们可以打印它了
for i in element:
    print ("element was:%d" %i)