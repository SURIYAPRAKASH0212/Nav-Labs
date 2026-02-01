n=int(input("n:"))
temp=n
small=0
min=1
while temp!=0:
  rem=temp%10
  temp=temp//10
  small=small+rem
  min=min*rem
if small%2==0 and min%3==0:
    print("Valid")
else:
    print("Invalid")