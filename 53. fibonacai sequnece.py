t = int(input('how many terms = '))
a = 0
b = 1
w = "nothing happens"
if t == 1 or t == 0:
    print(w)
elif t>1:
    print(a)
    print(b)
    for i in range(1,t):
        c = a+b
        print(c)
        a,b = b,c