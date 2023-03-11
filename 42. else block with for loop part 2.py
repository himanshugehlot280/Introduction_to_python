n = 1
for i in range(1, 11):
    if n == 5:
        break
    print(n, end=' ')
    n = n + i - 2
else:
    print(n, 'loop finished')
'''-----------------------------------'''
n = 1
for i in range(1, 11):
    if n == 5:
        break
    print(n, end=' ')
    n = n + i - 2 * i
else:
    print(n, 'loop finished')
'''-----------------------------------'''
# quiz type question
n = 1
for i in range(1, 11):
    print(i, end=' ')
    i = i * i
'''------------------------------------'''
