n=int(input("Enter n: "))
temp=n
a=0
while temp!=0:
  a=a+temp%10
  temp//=10
if a%9==0:
    print("valid")
else:
    print("invalid")