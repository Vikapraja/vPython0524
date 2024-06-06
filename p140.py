#Data Encapsulation
    #It is a techniquen to prevent accesss of data members of a class by unuthorized code(outerside class) directly.
    #Outerside class code can data access data members by methofes of class.

#Without encapsulation
class emp:
    def __init__(self):
        self.sal=50000

e=emp()
print(e.sal)

#with encapsulation
class emp:
    def __init__(self):
        self.__sal=50000

    def getsal(self):
        return self.__sal

e=emp()
#print(e.__sal)  #error

print(e.getsal())
