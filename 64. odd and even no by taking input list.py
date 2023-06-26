a = []
b = []
c = []
s = int(input("Enter a size of list: "))
for i in range(s):
    num = int(input("Enter a numbers: "))
    a.append(num)
print(a)
for i in a:
    if i % 2 == 0:
        b.append(i)
    else:
        c.append(i)

print("even number list", b)
print("odd number list", c)


