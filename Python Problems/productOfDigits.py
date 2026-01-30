n=int(input("Enter n:"))
pro=1
while n>0:
    pro*=n%10
    n//=10
print("Digit Sum:",pro)