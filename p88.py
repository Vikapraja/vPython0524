#if key is same then add values

d1={'a':100,'d':300,'c':200}
d2={}

for k0 in d0.keys():
    for k1 in d1.keys():
        if k0==k1:
            d2[k0]=d0[k0]+d1[k1] #indexing in dict
        else:
            continue

print(d2)
print('--------------------')
for k2,v2 in d2.items():
    print(k2,v2)

print('--------------------')
#check? dict is empty?

d3={}
if len(d3)==0:
    print('Empty')
else:
    print('not empty')

#dict comprehension
d3={i:j for i in range(11) for j in range(5,51)}
print(d3)
print(type(d3))

















