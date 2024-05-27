#2. Write a Python program to change a given string to a new string
#where the first and last chars have been exchanged. 

s='Vivekanand'
c=0
b=''
#print(type(b))
for i in s:
    if c==0:
        b+=s[-1]
    elif c==(len(s)-1):
        b+=s[0]
    else:
        b+=s[c]
    c+=1
print(b)

print('kkkk')
s1=str(input('enter str='))
def stri(a):
    if len(a)<2:
        return a
    return a[-1]+a[1:-1]+a[0]

d=stri(s1)

print(d)











    
