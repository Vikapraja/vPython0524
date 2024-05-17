bal=float(input('Enter intial bal='))
option=input('''Select your option
d. deposit
w. withdrow
c. check balance
''')

if option=='c':
    print(f'Available Bal={bal}')
elif option=='d':
    amt=float(input('Enter amount='))
    bal=bal+amt
    print(f'Updated Bal={bal}')
elif option=='w':
    if bal>=500:
        amt=float(input('Enter amount='))
        if bal>=amt:
            bal=bal-amt
            print(f'Updated Bal={bal}')
        else:
            print('you can not withdrow as bal is < 500')
    else:
        print('you can not withdrow as bal is < 500')
else:
    print("Invailid option")
