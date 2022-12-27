# or operator truth table
"""
condition1   condition2   output
    T             T          T
    T             F          T
    F             T          T
    F             F          F
"""
a = 50
print(a>0 or a<=100)
print(a>0 or a<=100 or a == 50)
print(a>0 or a<=100 or a == 10)
print(a>0 or a<=100 or a == 50 or a%10 == 0)
print(a>0 or a<=100 or a == 67 or a%10 == 0)
