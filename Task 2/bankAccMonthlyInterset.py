n=int(input("n:"))
ans=0
if n<+10000:
  ans=n*0.03
elif n>10000 and n<50000:
  ans=n*0.05
elif n>=50000:
  ans=n*0.07
print("monthly intrest amount:",ans/12)