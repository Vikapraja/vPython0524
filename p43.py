#Nested condition
        #it is a condition which is define inside other condition


mpin=int(input('Enter mpin='))
if mpin==1111:  #Top-level condition 
    print('welcome')
    otp=int(input('enter otp='))
    if otp==1234:   #nested condition
        print('vailid otp')
    else:
        print('invailid otp')
else:
    print('Invailid mpin')
