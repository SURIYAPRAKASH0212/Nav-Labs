n=int(input("n:"))
lf=0
if n<=2:
  lf=n*20
elif n>2 and n<=5:
  lf=40+((n-2)*15)
elif n>5:
  lf=85+((n-5)*10)
print(lf)