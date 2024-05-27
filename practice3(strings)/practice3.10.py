#10. Write a Python program to print the index of each character in a string.
a=[]
s=str(input('Enter a str=>'))
print(f'str->{s}')
for i in range(len(s)):
        a.append(i)
print(f'idx->{a}')
    
