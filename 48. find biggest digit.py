n = int(input("enter any number that you want"))
b = 0
sb = 0 #sb used for finding second biggest digit
while n>0:
    r = n%10
    if r>b:
        b=r
    elif r > sb and sb != r: # used for finding second big digit
        sb = r
    n = n//10
print(b)
print(sb)