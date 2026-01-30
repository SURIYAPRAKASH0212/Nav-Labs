amount=int(input("Enter Amount: "))
balance=int(input("Enter Balance Amount: "))
if amount%100==0 and amount<balance:
    balance-=amount
    if balance>=500:
        print("Success")
    else:
        print("Failed")
else:
    print("Failed")