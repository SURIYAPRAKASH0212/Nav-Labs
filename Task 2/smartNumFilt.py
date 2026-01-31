def prime(n):
  c=0
  for i in range(1,n+1):
    if n%i==0:
     c+=1
  if c==2:
    return(n)
  else:
    return(0 )
n=int(input("Enter n:"))
t=n
c=0
while t!=0:
  r=t%10
  t=t//10
  a=prime(r)
  c=c+a
print(c)