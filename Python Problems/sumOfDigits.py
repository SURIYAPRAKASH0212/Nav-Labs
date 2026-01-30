n=int(input("Enter n:"))
sum=0
while n>0:
    sum+=n%10
    n//=10
print("Digit Sum:",sum)