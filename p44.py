#Nested condition
        #it is a condition which is define inside other condition


mpin=int(input('Enter mpin='))
if mpin==1111:
    print('welcome')
    otp=int(input('enter otp='))
    if otp==1234:
        print('vailid otp')
    else:
        print('invailid otp')
else:
    print('Invailid mpin')
