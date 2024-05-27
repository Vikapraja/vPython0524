#5. Write a Python program to remove an item from a set if it is present
#in the set.

s={1,5,71,'hi','hello','bye'}
print(s)
for i in s:
    print(type(i),i)

b=str(input('Which type item  you to remove? \n1)str\n2)int\nChoose option (1/2)='))
if b=='1':
    a=str(input("Enter an item to remove which is in the set="))
elif b=='2':
    a=int(input("Enter an item to remove which is in the set="))
else:
    print('invailid option')



if a in s:
    s.remove(a)
    print('aftr remove=',s)
else:
    print('item not in the set')















    
