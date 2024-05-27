#18. Write a Python program to capitalize first and last
#letters of a given string.

s=str(input("Enter a str=>"))
a=''
for i in range(len(s)):
    if i==0:
        a+=s[0].upper()
    elif i==len(s)-1:
        a+=s[-1].upper()
    else:
        a+=s[i]

print(a)
