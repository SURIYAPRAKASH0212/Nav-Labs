t1=int(input("Enter angle 1: "))
t2=int(input("Enter angle 2: "))
t3=int(input("Enter angle 3: "))
if t1>0 and t2>0 and t3>0:
    if t1==t2==t3:
        print("Equilateral")
    elif t1==t2 or t1==t3 or t2==t3:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Invalid Input")        