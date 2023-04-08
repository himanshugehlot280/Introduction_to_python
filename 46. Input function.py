"""
Input Function
the input() function allows user input default it store string
"""
a = input('enter a number ')
print(a, type(a))
b = int(input('enter a number '))
print(b, type(b))

c = int(a)
print(b + c)
# print(b+a) it generate error

'''create series with input function with the help of while loop'''
start = int(input('enter starting of a loop '))
end = int(input('enter ending of a loop '))
jump = int(input('enter jump of a loop '))
i = start
print('while loop')
while i <= end:
    print(i, end=' ')
    i = i + jump
print('')
# create series with input function with the help of for loop
print('for loop')
for i in range(start, end, jump):
    print(i, end=' ')
