#String Methods
    #it orovides facility to perform string related operation
    #Syntax:
        #strVar.methode()
        #strValue.method()

s="ducat iNdia"
print(s.lower())#or
print("ducat iNdia".lower())#or
a=s.lower()
print(a)
print(s)

#Note:
    #string is immutable/unmodifiable,it means any change in str does not
    #effect existing string and a new copy gets created.

    #if we want to use result of operation then we need to store
    #result into a variable.

print(s.upper())#returns a new str with all upper letters
print(s.capitalize())#returns a  new str with first letter as upper else in lower
print(s.swapcase())#lower-->upper & upper-->lower

s=' virat kohali '
print(s)
print(s.lstrip())#removes leding/left spaces from string
print(s.rstrip())#removes trailling/right spaces from string
print(s.strip())#removes both left & right spaces from str

s="2024 welocome to python codding"
print(s.count('o'))
print(s.count('on'))
print(s.count(' '))
print(s.count('2'))
print(s.replace('o','z'))
print(s.replace('2','z'))

#string is itterable: we can get all chars of a string using for loop one by one
for x in s:
    print(x,x.count(x),x.upper())


