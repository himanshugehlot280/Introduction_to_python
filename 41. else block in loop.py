# Else Block with loop in python
"""Else block will execute after successfully execution of loop but if loop will terminate
by break keyword then else block will not execute.
The else block just after for/while is only executed when the loop is not terminated by
a break statement"""

for i in range(1, 11):  # loop is starting
    # --> this is the space of loop
    if i == 5: # condition statement
        # --> this space is refer to if block
        break
        # print(i) --> in this print statement is written in if block that's why
        #it not print when 5 is come then it break so it not generate any output
    print(i) # this print statement is work because it is written in loop block
    #that's why increment value we get from this print statment
else: # this else block work with for loop not with if statment
    print('after successful execution of loop')

