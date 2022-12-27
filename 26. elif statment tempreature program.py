#elif
''' the elif keyword is python way of saying if previous condition were not true,
then try this statment'''
''' Python has a built in module that you can use to make random numbers which is called random'''
import random
t = random.random()   # Here 1st random is module and 2nd random is function of the random module
t = int(t*100)      # random() -- Returns a random float number between 0 and 1  (W3 school)
if t>0 and t<=10:
    print('very low')
elif t>10 and t <=20:
    print('low')
elif t>20 and t <=30:
    print('normal')
elif t>30 and t<=40:
    print('high')
elif t>40 and t<=50:
    print('very high')
else:
    print('danger alert')