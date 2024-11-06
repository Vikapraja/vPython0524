import os
print("\t\t\t\tWelcome to my Automation Tool")
print("\t\t\t\t-----------------------------")

print("Option 1: Open notepad")
print("Option 2: Open Chrome")
print("Option 3: Send Whatsapp")

choice = input("Enter your choice: ")
print(choice)

if int(choice) == 1:
    os.system("notepad")
elif int(choice) == 2:
    os.system("Chrome")
elif int(choice) == 3:
    print("WA")
else:
    print("idk(i don't know)")