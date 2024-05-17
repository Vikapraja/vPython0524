#dict
        #it is a group of items there each item is represented by
        #key:value pair.

        #keys are unique and values can be duplicate

        #we uae keys to update/get values

        #it is mutabale

        #it maintainins order of kays

#syntax
    #var={}
    #var={key:value,key:value,....}
        #here (key:value)= item

d={101:'Virat',105:'rohit',102:'Surya',102:'bumrha',200:'virat'}
print(type(d))
print(d)
print(d[105]) #returns the value of given key,error if key not found

d[200]='jadeja'
print(d)

d[300]='dubey'
print(d)

d.pop(101)  #removes item based on given key,error if not found
print(d)

del d[105]  #remove item based on given key,erro if not found
print(d)















