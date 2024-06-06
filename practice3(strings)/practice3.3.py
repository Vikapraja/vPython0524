#3. Write a Python program to remove the characters which have odd index values of a given string

s=str(input('enter a str='))
print(len(s))
t=''
for i in range(len(s)):
    if i%2==0:
        continue
    else:
        t+=(s[i])

        
print(t)

#s=str(input('enter a str='))
#def r(s):
    
