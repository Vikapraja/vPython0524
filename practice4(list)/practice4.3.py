#3. Write a Python program to count the number of strings where the string
#length is 2 or more and the first and last character are same from a given
#list of strings.

li=['abc', 'xyz', 'aba', '1221','a']
a=0
b=[]
for i in li:
    if type(i)==type(''):
        if len(i)>=2:
            if i[0]==i[-1]:
                a+=1
                b.append(i)
for j in b:
    continue
print(a,b,sep=" >")
