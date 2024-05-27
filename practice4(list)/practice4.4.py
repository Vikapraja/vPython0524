#4. Write a Python program to remove duplicates from a list

li=[1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1]
a=[]
for i in li:
    if i in a:
        continue
    else:
        a.append(i)

print(f'before={li}\nafter={a}')
#or
b=[]
for j in li:
    if j not in b:
        b.append(j)
print(b)
