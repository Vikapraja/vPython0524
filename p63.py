#Indexing in str
    #For each chars python asigns index
    #There are 2 types of indexing
        #positive index(Start from 0 with first char then 1,2,3,4,...)
        #negative index(Start from -1 with last char then -2,-3,-4,...)
    #subscript operator is used to access a char using index
    #Syntax:
        #strVar[index]
        #strVal[index]

s='india'
print(s[0])
print(s[-4])
#print(s[6])#error: index is out of range

print(s.index('i'))#lowest index
print(s.rindex('i'))#highest index

s='abcabab'
print(s.index('a',2))#lowest index from 2 position(index)

#Note: str is immutable, we cann't assign or delete a char
    #s[0]='k'    #Error
    #del s[0]    #Error














