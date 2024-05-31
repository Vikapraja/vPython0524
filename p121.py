print("hi")
li=[10,20,30,40]
try:
    index=int(input("Enter index[0-3]="))
    print(li[index])
except IndexError:
    print("index out of range...")
except ValueError:
    print("Invailid index....")
print("bye")
