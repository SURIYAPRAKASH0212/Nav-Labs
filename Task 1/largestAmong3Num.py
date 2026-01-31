a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
if a>b and a>c:
    print("Largest: ",a)
elif b>a and b>c:
    print("Largest: ",b)
else:
    print("Largest: ",c)