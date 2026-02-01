n=int(input("n:"))
latefee=0
if n<=5:
  latefee=n*2
elif n>5 and n<=10:
  latefee=10+((n-5)*3)
elif n>10:
  latefee=25+((n-10)*5)
print("Late Fee:",latefee)