#Multilevel Inheritance
class telephone:
    def makecall(self):
        print("This is makecall")

class mobile(telephone):
    def msg(self):
        print("this is msg")

class smartphone(mobile):
    def vcall(self):
        print("this is vcall")

obj=smartphone()
obj.makecall()
obj.msg()
obj.vcall()
