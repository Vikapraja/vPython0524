#7. Write a Python program to print the numbers
#of a specified list after removing even numbers from it

li=[1,2,3,6,7,8,9,10,11,12]
a=[]
print(f'before={li}')
for i in li:
    if i%2==0:
        continue       
    else:
        print(i)

