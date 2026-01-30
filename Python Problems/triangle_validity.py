t1=int(input("Enter angle 1: "))
t2=int(input("Enter angle 2: "))
t3=int(input("Enter angle 3: "))
if t1>0 and t2>0 and t3>0:
    sum=t1+t2+t3
    if sum==180:
        print("Valid")
    else:
        print("invalid")
else:
    print("Invalid")