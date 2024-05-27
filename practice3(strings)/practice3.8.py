#8. Write a Python program to remove all newlines in a string.  

s=str('''My name is vivekanand.
i belongs to noida. ''')#input('''Enter str='''))

a=''

for i in s:
    if i=='\n':
        a=s.replace('\n',' ')
    else:
        continue
    
print(a)
