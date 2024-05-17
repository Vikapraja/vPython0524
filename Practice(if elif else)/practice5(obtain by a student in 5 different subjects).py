'''The marks obtain by a student in 5 different subjects are input
through keyboard. The student gets the division as per the
following rules:
Percentage above or equal to 60- first division
Percentage between 50 and 59- second division
Percentage between 40 and 49 – third division
Percentage below 40- fails.'''

print("all sub out of 100 marks:\n")
hindi=float(input("Enter obtain Hindi marks ="))
english=float(input("Enter obtain English marks ="))
math=float(input("Enter obtain Maths marks ="))
science=float(input("Enter obtain Science marks ="))
computer=float(input("Enter obtain Computer marks ="))

total=hindi+english+math+science+computer
per=(total/500)*100

if per>=60:
    print(f"{per} First division")
elif per<=59 and per>=50:
    print(f"{per} Second Division")
elif per<=49 and per>=40:
    print(f"{per} Third Division")
elif per<40:
    print(f"{per} Fail")
