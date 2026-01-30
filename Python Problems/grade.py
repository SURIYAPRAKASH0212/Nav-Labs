n=int(input("Enter Marks: "))
if n<0 or n>100:
    print("Invalid")
elif n>=91:
    print("Grade: O")
elif n>=81:
    print("Grade: A+")
elif n>=71:
    print("Grade: A")
elif n>=61:
    print("Grade: B+")
elif n>=51:
    print("Grade: B")
elif n>=41:
    print("Grade: C+")
else:
    print("Grade: U")