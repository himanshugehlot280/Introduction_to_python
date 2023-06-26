'''
# else block with python
s = '123456789'
for i in s:
    if i == '15':  # '1':
        break
    print(i)
else:
    print('else block is running')
'''
# --- factorial program ---
f = 1
n = int(input("enter a value "))
for i in range(1,n+1):
    f = f * i
print(f)