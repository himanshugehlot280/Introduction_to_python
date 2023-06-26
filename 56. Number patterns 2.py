n = int(input("enter a digit "))

for i in range(1, n + 1):
    if n == 0:
        break
    for j in range(2, i * 2, 2):
        print(j, end=" ")
    print(" ")
print("exit")
print("-------------------------------------------")

n1 = int(input("enter a digit "))
for i in range(1, n1 + 1):
    for j in range(n1 + 1 - i, 1, -2):
        if j % 2 == 1:
            continue
        print(j, end=" ")
    print(" ")
