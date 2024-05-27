#13. Write a Python program to swap comma and dot in a string.  
#Sample string: "32.054,23"
#Expected Output: "32,054.23"


def dotcom(s):
    a = str.maketrans(",.", ".,")
    b = s.translate(a)
    return b

s = "Hello, world. This is a test, string."
c = dotcom(s)
print("Original string:", s)
print("Swapped string: ", c)
