id=int(input("Enter Employee ID: "))
if len(str(id))==6:
    if id%7==0:
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")