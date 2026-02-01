n=int(input("Enter n: "))
for i in range(n):
  t=int(input("Temp: "))
  if t<45:
    print("Safe")
  else:
    print("Alert")
    break