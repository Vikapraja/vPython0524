import os
li=os.listdir("abc")
x=1
for i in li:
    os.rename(f"abc/{i}",f"abc/file-{x}.txt")
    x+=1
print("done")
