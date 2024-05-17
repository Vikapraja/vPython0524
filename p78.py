#dict methods

d={101:'sonu',102:'monu',103:'chintu'}

#how to iterate keys
for i in d.keys():
    print(i)

#how to iterate values
for i in d.values():
    print(i)

#how iterate item(bothe keys & values)
for k,v in d.items():
    print(k,v)

#how to iterate keys
for i in d():       #default kays for iterate
    print(i)
