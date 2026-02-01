n=int(input("n:"))
t=n
c=0
co=0
while t!=0:
  c=c+t%10
  t=t//10
  co=co+1
if c>15 and co==4:
    print("acces granted")
else:
    print("acces denied")