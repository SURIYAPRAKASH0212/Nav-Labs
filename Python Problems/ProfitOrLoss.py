cp=int(input("Enter Cost Price: "))
sp=int(input("Enter Sell Price: "))
p=cp-sp
if cp<0 or sp<0:
    print("Invalid CP or SP")
elif cp<sp:
    print("Profit:",abs(p))
else:
    print("Loss:",abs(p))