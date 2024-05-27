#

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
    
