n=int(input("n:"))
print("completed:",n//6)
if n%6==0:
  print("remaining:0")
else:
  print("remaining:",6-(n%6))