# change element in list
a = [10, 20, 30, 0, 50]
a[3] = 40
# [index position]
print("a with change", a)

# copy function use in list

b = a.copy()
print("b with copy", b)
a.append(60)
print("a with append", a)
print("b copy vala or a append", b)

# find function of anything
c = dir(list)
print(c)

# count function in list
a = [10, 20, 30, 40, 50]
i = a.count(10)
print("how many 10 in list = ", i)
