#WAP to test a whether a number is divisible by 3 or 5 or both.

a=float(input('Enter a number='))
b=3
c=5
if a%b*c==0:
    print(f"{a} is divisible by 3 and 5 both")
elif a%5==0:
    print(f'{a} is divisible by 5 ')
elif a%3==0:
    print(f"{a} is divisible by 3 ")
