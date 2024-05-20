#return statement

def add(a,b):
    c=a+b
    return c

res=add(4,5)
print(res)
#print(c)#error: c is local var so cann't accessable out of function    

print('----------------------------')
#define similar funct

def mul(a,b):
    d=a*b
    return d

m=mul(4,5)
print(m)

print('----------------------------')

def arithmetic(a,b):
    c=a+b
    d=a*b
    return c #after 'return' statement functions are end 
    return d #not executed

print(arithmetic(5,6))


print('----------------------------')
def arithmetic(a,b):
    c=a+b
    d=a*b
    return c,d #tuple

print(arithmetic(5,6))


print('----------------------------')
def result(marks):
    if marks>=40:
        return "pass"
    else:
        return "fail"

print(result(58))
print(result(39))


print('----------------------------')
#define similar function for even/odd

def check(num):
    if num%2==0:
        return "even"
    else:
        return "odd"

print(check(58))
print(check(39))


print('----------------------------')
#default return is None
def show():
    a=5

print(show())

