s=int(input())
n =int(input())
for _ in range(n):
    if s > 0:
        print("BOOKED")
        s -= 1
    else:
        print("HOUSEFULL")
        break
else:
  print(s)