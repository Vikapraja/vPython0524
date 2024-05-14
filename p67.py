#creating empty list
li=[]
print(type(li))
print(li)

#creating list with intial value
li=[10,20,10,30,40,6.7,'hi']
print(li)

#list is iterable(fetching values one by one by for loop)
for x in li:
    print(x)

#slicimg/indexing in list
print(li[-1])
print(li[0])
print(li[::-1])

#list is mutable/changeable/moifiable
li[0]=100
print(li)

