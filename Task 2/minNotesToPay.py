n=int(input("Enter Amount: "))
temp=n
if temp>=500:
  n1=temp//500
  temp=temp-(n1*500)
  print("500 -",n1 if n1>0 else None)
if temp>=200:
  n1=temp//200
  temp=temp-(n1*200)
  print("200 -",n1 if n1>0 else None)
if temp>=100:
  n1=temp//100
  temp=temp-(n1*100)
  print("100 -",n1 if n1>0 else None)
if temp>=50:
  n1=temp//50
  temp=temp-(n1*50)
  print("50 -",n1 if n1>0 else None)
if temp>=20:
  n1=temp//20
  temp=temp-(n1*20)
  print("20 -",n1 if n1>0 else None)
if temp>=10:
  n1=temp//10
  temp=temp-(n1*10)
  print("10 -",n1 if n1>0 else None)
if temp>=1:
  print("1 -",temp if n1>0 else None)