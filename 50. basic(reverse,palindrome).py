n = int(input("enter a number for reverse "))
reverse = 0
while n > 0:
    r = n % 10
    reverse = reverse * 10 + r
    n = n // 10
print(reverse)
"""--------------------------------------------------"""
n = int(input("enter a number for palindrome "))
t = n
reverse = 0
while n > 0:
    r = n % 10
    reverse = reverse * 10 + r
    n = n // 10
if t == reverse:
    print("palindrome")
else:
    print("not palindrome")
"""----------------------------------------------------"""
# NOTE : len function not work with integer that's why we take input in string
n = input("enter a value for armstrong ")
s = len(n)
n = int(n)
t = n
rv = 0
while n > 0:
    r = n % 10
    rv = rv + r ** s
    n = n // 10
if rv == t:
    print('armstrong')
else:
    print("not armstrong")


