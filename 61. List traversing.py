"""
Traversing of list
there are two types of traversing available in list
1. index wise traversing
2. element wise traversing
"""

a = [10,20,30,40,50,30,20]
print("index wise traversing")
for i in range(0,len(a)):
    print(a[i])
print("-----------------------------------------------")
print("element wise traversing")
for i in a:
    print(i)