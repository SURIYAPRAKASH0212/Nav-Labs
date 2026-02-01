l=float(input("liter:"))
p=float(input("price:"))
to=int(l*p)
last=to%10
if last<5:
  to=to-last
else:
  to=to+(10-last)
print(to)