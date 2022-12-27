# Logical Operators
"""
logical operators are used to combine conditional statment

and :- return true if both statments are true
or  :- return true if one or more than one statments is true
not :- Reverse the result, returns False if the result is true
"""
# and operator truth table
"""
condition1   condition2   output 
    T             T          T 
    T             F          F 
    F             T          F 
    F             F          F 
"""
a = 50 
print(a>0 and a<=100)
print(a>0 and a<=100 and a == 50)
print(a>0 and a<=100 and a == 10)
print(a>0 and a<=100 and a == 50 and a%10 == 0)
print(a>0 and a<=100 and a == 67 and a%10 == 0)