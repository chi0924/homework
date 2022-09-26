number = [1, 2, 3, 4, 5, 6, 7]
list1 =  [1, 2, 3, 4, 5, 6, 7]
list2 = []
for i in range(len(number)):
    v1 = number[i]*list1[i]  #上下兩個相乘
    list2.append(v1)
print(list2)