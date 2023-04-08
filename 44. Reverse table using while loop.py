i = 5
n = i * 10
while i <= n:
    print(n,end=' ')
    n = n - i
print('')
'''---------------'''
#factorial program using while loop
i = int(input('enter a number for factorial --> '))
n = 1
while i>=1:
    n = n*i
    print(n,end=' ')
    i = i-1
    print(i,end=' ')
