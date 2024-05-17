#if cost price and selling price of an item is input through keyboard.
#write a program to check profit or loss.

cost=int(input('Enter cost price='))
selling=int(input('Enter Selling price='))
if selling>cost:
    print('Profit')
elif selling<cost:
    print('Loss')
elif selling==cost:
    print("No loss and no profit")
    
