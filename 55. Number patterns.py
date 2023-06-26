n = int(input("enter a digit "))
for i in range(1, n + 1):
    if n == 0:
        break
    for j in range(1, i + 1):
        print(j, end=" ")
    print(" ")
print("exit")
print("----------------------------------------------------")
print(" ")

n1 = int(input("enter a digit "))
wn1 = n1 + 1
for i in range(1, n1 + 1):
    if n1 == 0:
        break
    for j in range(1, wn1 - i):
        print(j, end=" ")
    print(" ")
print("exit")
print("----------------------------------------------------")
print(" ")

n2 = int(input("enter a digit "))
for i in range(1, n2 + 1):
    if n2 == 0:
        break
    for j in range(i, 0, -1):
        print(j, end=" ")
    print(" ")
print("exit")
print("----------------------------------------------------")
print(" ")

n3 = int(input(" enter a digit "))
for i in range(1, n3 + 1):
    if n3 == 0:
        break
    for j in range(1, i * 2, 2):
        print(j, end=" ")
    print(" ")
print("exit")
print("----------------------------------------------------")
print(" ")
