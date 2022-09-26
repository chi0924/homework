list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

list3 = []
for i in range(len(list1)):
    v1 = list1[i]+list2[i] #上下兩個相加
    list3.append(v1)
print(list3)