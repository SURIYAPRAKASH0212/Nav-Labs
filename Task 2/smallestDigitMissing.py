n=int(input("n:"))
temp=n
dlist=[0,1,2,3,4,5,6,7,8,9]
while temp!=0:
  r=temp%10
  temp//=10
  if r in dlist:
    dlist.remove(r)
print(dlist[0])