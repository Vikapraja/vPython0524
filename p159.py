#Multithreading 
    #It is a technique that runs multiple functions using timesharing concept.
    #Advantage of this technique is , it reduce waiting time of other independent function.

#Thread=> A thread is an independent execution in program.
        #In codding, A thread is an object of Thread class.

#real life example based on thrading
    #uploading/downloading
    #each tab in browser
    #wifi connection search in background
    #animation
    #speling checker in msword
    #each user in website
    #etc.

from threading import Thread
def check():
    num=int(input("Enter num="))
    if num%2==0:
        print("even")
    else:
        print("odd")

def change():
    import os
    os.rename("last.txt","players.txt")

t1=Thread(target=check)
t2=Thread(target=change)

t1.start()
t2.start()
