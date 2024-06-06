# Write a Python program to count the occurrence of words in a given string. 
s=str(input('Enter a str='))
c=0
d=s.split()
for i in d:
    print(i)
    c+=1

print('occurance of word in str=',c)
