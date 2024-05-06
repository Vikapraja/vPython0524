#continue & break keywords
while True:
    a=int(input('Enter a='))
    b=int(input("Enter b="))
    print(a*b)
    ch=input("Do you want to multiply again y/n?")
    if ch=='y':
        continue
    elif ch=='n':
        break

#continue: it is used to start next iteration of loop
#break: it is used to terminate loop(close next interation of loop)
