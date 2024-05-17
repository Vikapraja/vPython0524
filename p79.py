
d={101:'sonu',102:'monu',103:'chintu'}

#searching in dict
print('sonu' in d)
print('sonu' in d.values())


#sorting in dict
print(sorted(d))
print(sorted(d.values()))

#aggrregation
print(len(d))
print(min(d))
print(min(d.values()))

#dict comprehensio
    #syntax:
        #var={key_expression:value_expression for}
d={i+i:i*i for i in range(1,5)}
print(d)

a=[]
print(typr(a))

b=()
print(typr(b))

c={}#dict
print(typr(c))

d=set()#empty set only by set()
print(typr(d))

