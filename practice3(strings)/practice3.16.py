#16.Write a Python program to remove spaces from a given string.  


s=str(input("enter astring="))
a=''
b=0
for i in s:
    if i==' ':
        b+=1
        continue
    else:
        a+=s[b]
        b+=1
print(len(s),b)
print(a)
