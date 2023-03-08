n = int(input('enter a number, for printing a table '))
for i in range(n, n * 10 + 1, n):
    print(i, end=' ')
print(end='\n')
'''---------------------------------------------------------'''
n = int(input('enter a number, for printing a table '))
for i in range(1, 11):
    print(n, '*', i, '=', n * i)
