list1 = ["Hello", "take"]
list2 = ["Dear", "Sir"]
v1 = len(list1)
a1 = v1 // 2
b1 = list1[:a1]
c1 = list1[a1:] #分割list


v2 = len(list2)
a2 = v2 // 2
b2 = list2[:a2]
c2 = list2[a2:] #分割list


x = b1+b2
x = [' '.join(x)]
x2 = b1+c2
x2 = [' '.join(x2)]
x3 = b2+c1
x3 = [' '.join(x3)]
x4 = b2+c2
x4 = [' '.join(x4)]

total = x + x2 + x3 + x4 #各項相加並輸出
print(total)