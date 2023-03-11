# Syntax
"""
initialization
while True/False condition:
    statement
    increment/decrement"""

'''With the while loop we can execute a set of statements as long as a condition is true'''

i = 1
while i <= 10:
    print(i, end=' ')
    i = i + 1
print('after loop is finished')
'''---------------------------------'''
i = 1
while i <= 10:
    print(i, end=' ')
    i = i + 2
print('after loop is finished')
'''---------------------------------'''
i = 5
n = 1
while n <= 10:
    print(i * n, end=' ')
    n = n + 1
print('')
'''---------------------------------'''
x = 5
y = i
while x < y * 10 + y:
    print(x, end=' ')
    x = x + y
print('')
'''---------------------------------'''
n = 0
i = 0
while i <= 5:
    n = n + i
    i = i + 1
    print(n, i, end='|')
print(n)
'''----------------------------------'''
# Reverse no program using while loop
i = 10
while i>=1:
    print(i,end=' ')
    i = i-1
print('')
'''----------------------------------'''
# Reverse table print
i = 5
n = i
while i<=n*10:
    print(i,end=' ')
    i = i+n
