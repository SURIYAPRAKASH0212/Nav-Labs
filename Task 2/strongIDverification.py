def factorial(n):
  f=1
  for i in range(1,n+1):
    f=f*i
  return(f)
n=int(input("n:"))
t=n
c=0
while t!=0:
  r=t%10
  t=t//10
  c=c+factorial(r)
if c==n:
  print("Strong Number")
else:
  print("not a Strong Number")