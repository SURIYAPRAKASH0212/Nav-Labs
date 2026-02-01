b=int(input("batter:"))
d=int(input("drop:"))
hour=0
while b>20:
  b=b-d
  hour=hour+1
print(hour)