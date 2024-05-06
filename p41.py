cost=float(input('Enter the cost price of product='))
sell=float(input('Enter selling price of product='))
if sell>cost:
    print('Profit',sell-cost)
elif sell<cost:
    print('Loss',sell-cost)
elif cost==sell:
    print('No profit and No Loss equal')
