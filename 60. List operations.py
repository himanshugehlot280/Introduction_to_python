#extend
a = [10,20,30,40,50]
b = [60,70,80]
a.extend(b)
print("extend ", a)
print("----------------------------------------------")
#index
i = a.index(40)
print("index ", i)
print("----------------------------------------------")
#append
a.append(34)
print("append ",a)
print("-----------------------------------------------")
#insert
a.insert(0,110)
print("insert",a)
print("-----------------------------------------------")
#pop
a.pop()
print("pop",a)
print("-----------------------------------------------")
#remove
a.remove(20)
print("remove ",a)
print("-----------------------------------------------")
#reverse
a.reverse()
print("reverse ",a)
print("-----------------------------------------------")
#sort
a.sort()
print("sort ",a)
print("-----------------------------------------------")
a.sort(reverse=True)
print("sort2 ",a)

