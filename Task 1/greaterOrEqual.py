a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=a+b
d=a*b
if(c>d):
    print("(a+b) is greater than (a*b)")
elif(c<d):
    print("(a+b) is less than (a*b)")
elif(c==d):
    print("Equal")