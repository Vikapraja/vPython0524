#Multiple Inheritance
class telephone:
    def makecall(self):
        print("This is makecall")

class camera:
    def picture(self):
        print("this is picture")
              
class mobile(telephone,camera):
    def msg(self):
        print("this is msg")

obj=mobile()
obj.makecall()
obj.msg()
obj.picture()
