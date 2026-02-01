def prime(n):
  count=0
  for i in range(1,n+1):
    if n%i==0:
     count+=1
  if count==2:
    return(n)
  else:
    return 0
n=int(input("Enter n:"))
temp=n
count=0
while temp!=0:
  rem=temp%10
  temp=temp//10
  ans=prime(rem)
  count=count+ans
print(count)