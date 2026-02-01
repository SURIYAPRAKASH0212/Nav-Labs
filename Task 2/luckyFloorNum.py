n=int(input("n:"))
count=0
for i in range(n):
  temp=i
  check=0
  while temp!=0:
    r=temp%10
    temp=temp//10
    if r==4:
      check=1
      break
  if check!=1:
    count=count+1
print(count)