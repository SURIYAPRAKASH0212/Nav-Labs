n=int(input("n:"))
t=n
dlist=[0,0,0,0,0,0,0,0,0,0]
while t!=0:
  r=t%10
  t=t//10
  dlist[r]=dlist[r]+1
d=int(input("d:"))
print(dlist[d])