a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
x=b**2-4*a*c
if x>0:
    print("Real & Distinct")
elif x<0:
    print("Imaginary")
else:
    print("Real & Equal")