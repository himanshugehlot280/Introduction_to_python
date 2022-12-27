# Membership Operators
"""
Membership operators are used to test if a sequence is presented in an object.
in:- Returns True if a sequence with the specified value is present in the object
not in:- Returns True if a sequence with the specified value is not present in the object
"""
a = 'hello'
b = 'hello'
c = 'python'
print('working of in')
print(b in a)
print(c in a)
print('b' in a)
print('h' in a)
print('o' in b)
print('a' in b)
print('-----------------------')
print('working of not in')
print(b not in a)
print(c not in b)
print('b' not in a)
print('h' not in a)
print('o' not in b)
print('a' not in b)
