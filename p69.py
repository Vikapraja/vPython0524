#searching list
li=[10,20,30]
print(20 in li)

#sorting in list
li=[5,20,-5,50,26,29]
print(li)
print(sorted(li)) #asc order
print(sorted(li,reverse=True)) #des order

#Note: sorted() always returns a new list of sorted values
print(li)

    #aggregation in list(count/sum/min/max/avg/etc)
li=[2,4,6,8]
print(len(li))  #no of values
print(sum(li))
print(max(li))
print(min(li))
print(sum(li)/len(li))   #avg
