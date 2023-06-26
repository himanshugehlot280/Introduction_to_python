for i in range(1, 6):
    for k in range(1, i):
        print(" ", end="")
    for j in range(1, i + 1):
        print("*", end=" ")
    print(" ")

print("-----------------------------------------------------------------")

n1 = int(input("enter a digit "))
for i in range(1, n1):
    if n1 == 0:
        break
    for k in range(1, n1 - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print("*", end="")
    print(" ")
print("break")
print("-----------------------------------------------------------------")

n2 = int(input("enter a digit "))
for i in range(1, n2):
    if n2 == 0:
        break
    for k in range(1, n2 - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end="")
    print(" ")
print("exit")
print("-----------------------------------------------------------------")

for i in range(1, 6):
    for k in range(1, 6 - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print("*", end=" ")
    print(" ")

print("-----------------------------------------------------------------")

for i in range(1, 6):
    for k in range(1, 6 - i):
        print(" ", end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print(" ")

print("-----------------------------------------------------------------")

for i in range(1, 6):
    for k in range(1, 6 - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end="")
    for l in range(i - 1, 0, -1):
        print(l, end="")
    print(" ")
