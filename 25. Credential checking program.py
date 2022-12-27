id = 'Admin'
password = 'admin@123'

print('Welcome to an admin app')
a = input('please enter your id -> ')
b = input('enter your password -> ')
if a == id and b == password:
    print('welcome to admin panel')
    print('Here is your secret message --> Hello admin ')
else:
    print('you enter wrong id or password')
