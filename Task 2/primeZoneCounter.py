a=int(input("a:"))
co=-1
for j in range(1,a+1):
  c=0
  for i in range(1,j+1):
    if j%i==0:
      c+=1
  if c<=2:
    co=co+1
print(co)