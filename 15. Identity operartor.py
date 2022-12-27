#  Identity operators
"""
Identity operators are used to compare the objects, not if they are equal, but if they are actually
the same object, with the same memory location

is:- Returns True if both variables are the same object.
is not: - Returns True if both variables are not the same object.
"""
a = 'hello'
b = 'hello'
c = 'python'
d = a
print('working of is')
print(a is b)
print(a is c)
print(a is a)
print(a is d)
print('------------------')
print('working of is not')
print(a is not b)
print(a is not c)
print(a is not a)
print(a is not d)
