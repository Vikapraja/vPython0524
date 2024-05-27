#19.WAP to find number of occurrences of character ‘o’ in the string entered
#through keyboard. If the character ‘o’ is not present in the string then show
#a message “o is not present in the entered string”.


s=str(input("Enter a str=>"))
a=0
b=[]
for i in s:
    a+=1
    if i=='o':
        b.append(a-1)
        if s[a]==(len(s)-3):
            print('number of occurrences of character ‘o’ in the string=>',b)

    elif 'o' not in s:
        print('o is not present in the entered string')
    else:
        continue
print(b)
      
#or

if 'o' in s:
    print('y')

else:
    print('n')

















