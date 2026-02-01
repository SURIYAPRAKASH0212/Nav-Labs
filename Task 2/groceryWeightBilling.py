w=float(input("weight:"))
p=float(input("price:"))
c=w*p
if w<=10:
  print("amount:",c)
else:
  print("amount:",c-(c*0.05))