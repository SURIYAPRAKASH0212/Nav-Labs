n=int(input("n:"))
temp=n
odd=0
even=0
while temp!=0:
  rem=temp%10
  if rem%2==0:
    even+=1
  else:
    odd+=1
  temp=temp//10
print(even,odd)