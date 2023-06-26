n = int(input('enter a digit '))
WN = n + 1
for i in range(1, WN):
    if n == 0:
        break
    for j in range(1, i + 1):
        print('*', end=' ')
    print()
print("exit")
print("-------------------------------------")
print(" ")

n1 = int(input('enter a digit '))
wn2 = n1 + 1
for i in range(1, wn2):
    if n1 == 0:
        break
    for j in range(1, wn2 - i):
        print('*', end=" ")
    print(" ")
print("exit")
print("--------------------------------")
print(" ")

n2 = int(input("enter a digit "))
wn2 = n2 + 1
for i in range(1, wn2):
    if n2 == 0:
        break
    for j in range(1, i * 2):
        print("*", end=" ")
    print(" ")
print("exit")
print("--------------------------------")
print(" ")

n3 = int(input("enter a digit "))
wn3 = n3 + 2
# +2 because in for loop 1 values is deducted
for i in range(1, wn3):
    if n3 == 0:
        break
    for j in range(1, wn3-(i*2)):
        print("*", end=" ")
    print(" ")
print("exit")
print("--------------------------------")
print(" ")

