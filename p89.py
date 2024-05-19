#Function Parameters & Arguments
    #these concept provide facility to pass values of function
    #logic for each call.

    #i.e. for each call, we pass use same function according to our
    #requirement by passing differnt values.

    #Parameteres: are variables that we define  () of def
    #Arguments:are values of params that we pass at the time of further call of functions
    
def mul(a,b):   #a,b are parameters(local scope)
    print('multiplication=',a*b)

mul(3,4)   #3,4 are agruments
mul(2,6)   #2,6 are arguments
mul(12,8)   #12,8 are arguments

x=int(input('Enter x='))
y=int(input('Enter y='))

mul(x,y)    #x,y are arguments

    #Note:
        #for each call we need to pass same no of parameters as the no. of parameters 














