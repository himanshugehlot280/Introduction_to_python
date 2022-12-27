a = (input('enter a number '))
if a.isnumeric() == True:
    a = int(a)
    print(a ,'is a integer')
    if 0 < a and a <= 100:
        print(a, 'is within range')
    else:
        print(a, 'out of range')
else:
    print(a,'is a string')


