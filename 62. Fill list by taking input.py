a = []
s = int(input("enter a digit "))
for i in range(1, s + 1):
    print("enter element ", i)
    t = int(input())
    a.append(t)
    print(t, "append successfully")

print("element wise traversing")
for i in a:
    print(i)
print("index wise traversing")
for i in range(0, len(a)):
    print(a[i])
print("-----------------------------------------------")

# finding sum of input values
print("sum is ", sum(a))
