n = int(input('enter a seris of number '))
while n > 0:
    r = n % 10
    if r % 2 == 0:
        print('even number', r)
    else:
        print('odd number', r)
    n = n // 10
