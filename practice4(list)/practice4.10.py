#10. Write a Python program to get unique values from a list.

li=[1,2,3,4,4.5,4.5,4.6,'hi','hello','hi']
a=[]
for i in li:
    if i in a:
        continue
    else:
        a.append(i)

print(f'unique value list of given list={a}')
