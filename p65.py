#String slicing
    #obtaining a part/substring of a str
    #syntax:
        #strVar[startIndex:endIndex:step]

    #note:
        #startIndex----->inclusive
        #endIndex------->exclusive
        #step
            #+ve step---->forward slicing
            #-ve step---->reverse slicing

s='python'
print(s[1:4:1])
print(s[0:4:2])
print(s[5:0:-1])
print(s[-6:5:1])

print(s[1:5:]) #default step=1(step can not be zero)
print(s[1:5])  #default step=1

print(s[0::1]) #default end=slicing upto last char in forward
print(s[-1::1])#default end=slicimg upto last char in reverse

print(s[::2])  #default start=0 if step +ve 
print(s[:3:-1])#default start=-1 if step -ve

print(s[::-1]) #revrse slicing
#print(s[1:5:0])#error(step can not be zero)

print('-----------')

print(s[3:-1])#all chars from 3 chars 
print(s[-3:]) #last 3 chars
print(s[:3])  #3 chars from start
print(s[1:-1])# all middle chars of str

#string formatting
#string repeatation
#str concatenation
#str methods
#str searching
#str indexing
#str slicing












