n = int(input('enter a value '))

if n == 0 or n == 1:
    print(n, 'is not a prime no')
else:
    for i in range(2, n):
        if n % i == 0:
            print(n, 'n is not prime no')
            break
    else:
        print(n, 'is prime no')
print('------------------------------------------')
'''----------------------------------------------'''

w = int(input('enter a number '))
temp = 1
tp = 0
for i in range(1, w + 1):
    temp = temp * i
    tp = tp + i
print(temp)
