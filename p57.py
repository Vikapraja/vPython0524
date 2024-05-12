#table of 5
print("------5's table------")
num=5
x=1
for y in range(10): #without using loop's variable
    print(num*x)
    x+=1

#table of 5
print("------5's table------")
num=5
for x in range(1,11):   #using loop's variable
    print(num*x)

#break statement in for loop
print("------break stmt in for ------")
for x in range(1,20):
    print(x)
    if x>=18:
        print('valid for vote')
        break

