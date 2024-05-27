#12. Write a Python program to lowercase first n characters in a string.  

s=str(input('Enter a str='))
n=int(input("Enter a no to lowercase first n characters in a string ="))
l=s[:n:].lower()
print(l)

    
