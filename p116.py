#Regular expression(Regex)
    #it is a technique that matches strings based on a pattern.
    #It is widely used in :
        #data validation(checking username/password/email/....)
        #interpreter Design
        #data clearing

    #python provides a standard library 're'

text="""Python is a funny language created by Guido VAN Rossum.
It was first released in 1991.
I study python"""

import re
li=re.findall('i.',text)
print(li)

li=re.findall('i..',text)
print(li)

li=re.findall("i.[abcdefghijklmnopqrstuvwxyz]",text)
print(li)

li=re.findall("i.[a-z]",text)
print(li)

li=re.findall('[A-Z][a-z][aeiou][a-z]',text)
print(li)

li=re.findall('[A-Za-z][aeiou][a-z]',text)
print(li)

li=re.findall('[A-Za-z][aeiou][a-z]',text)
print(li)

li=re.findall('[A-Za-z][^aeiou][a-z]',text)#(^)-->It is for except/not
print(li)

li=re.findall('[A-Za-z][aeiou][a-z]{3}',text)#{3} repeatation
print(li)

text="""Python is a funny language created by Guido VAN Rossum.
It was first released in 1991.
I study python
"""

# li=re.findall('[A-Za-z][a-z]{3,5}',text)#{min,max} repeatation

li=re.findall('[A-Za-z][a-z]+',text)#{1,N} repeatation
print(li)

li=re.findall('[A-Za-z][a-z]*',text)##{0,N} repeatation
print(li)

li=re.findall('[A-Za-z][a-z]?',text)##{0,1} repeatation
print(li)

li=re.findall('[.]',text)#for dot
print(li)

li=re.findall('\.',text)#for \
print(li)

#Pre defind patterns
li=re.findall('\d',text)#[(0-9)]
print(li)

li=re.findall('\s',text)#[\n\t]
print(li)

li=re.findall(' \w',text)#[a-zA-Z0-9]
print(li)
























