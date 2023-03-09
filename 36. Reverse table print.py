n = int(input('Enter a number'))
for i in range(n*10,n-1,-n):
    print(i,end=' ')
print('\n')
'''-------------------------------------------------------------'''
n = int(input('enter a number, for printing a table '))
for i in range(10,0,-1):
    print(n, '*', i, '=', n * i)