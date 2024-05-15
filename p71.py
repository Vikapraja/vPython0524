#Wap to get unique value from list
li=[10,20,10,30,20,34]
y=[]
for i in li:
    if i not in y:
        y.append(i)
print(li)
print(y)

#list comprehension(creating a list with single stmt by for loop)
li=[x*x for x in range(1,5)]
print(li)

s=[1+x for x in range(1,10)]
print(s)

#to do empty to list(.clear())
s.clear()
print(s)









