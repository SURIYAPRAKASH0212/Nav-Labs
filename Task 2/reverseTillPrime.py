n=int(input("n:"))
t=n
r=""
while t!=0:
  l=t%10
  t=t//10
  r=r+str(l)
r=int(r)
c=0
for i in range(1,r+1):
  if r%i==0:
    c+=1
if c==2:
  print("prime")
else:
  print("not prime")