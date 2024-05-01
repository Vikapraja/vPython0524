#Membership Operator
    #in------>True if element is a member else False
    #not in-->True if element is not a member else False

s="welcome to python"
print('c' in s)
print('c' in 'welcome')
print('k' in s)
print('to' in s)
print('to' not in s)
print('k' not in s)
#print(2 in 123) #error(only works with iterable(str/list/tuple/..))
print('2' in '123')

#digit as char------->'5'
#digit as number----->5

#Del operator
    #to delete a variable sothat it can not be used in further
    #statements of program

print(s)
del s
#print(s) #error

s="......."
print(s)

#Note:del operator can not be used to delete a value.
#del 5 #error





