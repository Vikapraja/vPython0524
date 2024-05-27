#11. Write a Python program to check if a string contains all vowels of the alphabet.

s=str(input('Enter a str='))
a=set(s)
b=set('aeiouAEIOU')

if b.issubset(a):
    print('yes str contains all vowel')
else:
    print('str not contain all vowel')
    
#print(a)
