pin=9342
a=0
while a!=3:
  a=a+1
  ans=int(input("Enter PIN: "))
  if ans==pin:
    print("Acces Granted")
    break
  else:
    if a<3:
      print("try again")
if a==3:
  print("Card Block")