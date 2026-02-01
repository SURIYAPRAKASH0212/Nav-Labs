n=int(input("Enter n: "))
min=1000000
for i in range(n):
  a=float(input())
  if a<min:
    min=a
print("Fastest Runner:",min)