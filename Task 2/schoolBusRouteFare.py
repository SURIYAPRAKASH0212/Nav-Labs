n=int(input("Enter n:"))
f=0
if n<6:
  f=n*10
elif n>5 and n<16:
  f=50+((n-5)*8)
elif n>15:
  f=130+((n-15)*6)
print(f)