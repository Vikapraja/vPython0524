#set
    #it is a group of unique values
    #it does not maintain order
    #it does not support indexing & slicing
    #it is iterable
        #Syntax:
            #var={v1,v2,v3,.....}

s={10,20,30,-40,50}
print(type(s))
print(s)
#print(s[0]) #error

#iterable(fetchng values one by one through for loop)
for i in s:
    print(i)

#set methods
    #setVar.method(args)

#how to add a value
s.add(13)
print(s)

#how to remove value
s.remove(10)
print(s)

#how to remove value randomely
s.pop()
print(s)



















