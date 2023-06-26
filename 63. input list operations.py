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

# finding max and min following two ways
a.sort()
print("min is ",a[0])
print("max is ",a[len(a)-1])
print("-----------------------------------------------")
# 2nd way
print("min is ",min(a))
print("max is ",max(a))