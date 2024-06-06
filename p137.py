#Hierarchical inheritance

class person:
    def think(self):
        print('this is think')
    def eat(self):
        print("this is eat")

class student(person):
    def study(self):
        print('this is study')

class actor(person):
    def acting(self):
        print('thisis acting')

obj=student()
obj.think()
obj.eat()
obj.study()

obj=actor()
obj.think()
obj.eat()
obj.acting()
