n=int(input("total stair:"))
k=int(input("stair in 1 step:"))
print("step needed",n//k)
if n%k!=0:
  print("stair remaining",n%k)