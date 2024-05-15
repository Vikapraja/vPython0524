#Tuple
    #it is unmodifialbe/immutable
    #other concept are same as list.
        #syntax:
            #var=()
            #var=(value1,value2,.....)

#creating empty tuple
t=()
print(type(t),t)

#creating tuple with value
t=(10,20,30,10)
print(t)

#creating tuple with single value
t=(10)
print(type(t))
t=(10,)
print(type(t),t)

#creating tuple with str
t=tuple('ducat')
print(t)

#creating tuple with range
t=tuple(range(1,11))
print(t)

#creating tuple with list
t=tuple([10,20,30,40])
print(t)

#t[0]=100  #error:unmodifiable
#t.pop




