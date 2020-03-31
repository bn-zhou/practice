i = 0
numbers = []


while i < 6:
    print ("在顶部i是%d。" %i)
    numbers.append(i)

    i = i + 1
    print ("现在数字是：",numbers)
    print ("在底部i是%d" %i)


print ("数字是")

for num in numbers:
    print (num)

