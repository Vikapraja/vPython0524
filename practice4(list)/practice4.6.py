#Write a Python program to print a specified list after removing the 0th, 4th
#and 5th elements.

#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']


li=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
a=[]
for i in li:
    if i==li[0]:
        continue
    elif i==li[4]:
        continue
    elif i==li[5]:
        continue
    else:
        a.append(i)
print(f'list after removing the 0th, 4th and 5th elements{a}')
