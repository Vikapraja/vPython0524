#Write a program to print counting from 20 to 0 with gap 2 usig for loop
print('----20 to 0 with gap 2 using for loop -----')
for x in range(20,-2,-2):
    print(x)

#write a program to print counting from -5 to +5 With gap1
print('----(-5)to(+5) using for loop------ ')
for i in range(-5,6,1): #for x in range(-5,6):
    print(i)            #   print(x)

# Write a program to print even/odd no from 1 to 10
print('-----Even/odd for (1 to 10)using for loop------')
for i in range(1,11):
    if i%2==0:
        print(i,'is even')
    else:
        print(i,'is odd')

#wap progame for range arguments
print("----progame for range's arguments-----")
a=int(input('Enter start='))
b=int(input('Enter end='))
c=int(input('Enter step='))

for x in range(a,b,c):
    print(x)

