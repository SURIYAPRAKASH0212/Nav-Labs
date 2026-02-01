n=int(input("n:"))
temp=n
check=0
while temp!=0:
  rem=temp%10
  temp=temp//10
  if rem==0:
    check=1
if check==1 and n%10==5:
    print("Open")
else:
    print("Locked")