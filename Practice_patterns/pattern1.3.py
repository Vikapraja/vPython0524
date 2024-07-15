#pattern 3

x=1
for i in range(1,6):        #Controls rows
    for j in range(0,i):    #controls cols in each rows
        print(x,end=" ")     #controls numbers which we want to print with proper space
        x+=1
    print("")               #provide new lines for rows
