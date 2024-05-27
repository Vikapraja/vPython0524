#6. Write a Python program to convert a given string to all uppercase
#if it contains at least 2 uppercase characters in the first 4 characters.  

s=str(input('Enter given str='))
a=0
b=''
for i in s[0:5]:
    if i.isupper():
        a+=1
        if a>=2:
            break
    else:
        continue
    
if a>=2:
    u=s.upper()
    print(f'Str in uppercase={u}')
else:
    print('At least 2 In first 4 chars of str should be upper to convert str to all uppercase')

    
    






    
