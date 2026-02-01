n=int(input("Enter Amount:"))
discount_amount=0
if n>=5000:
  discount_amount=n-(n*0.3)
elif n<5000 and n>=3000:
  discount_amount=n-(n*0.2)
elif n<3000 and n>=1000:
  discount_amount=n-(n*0.1)
elif n<1000:
  discount_amount=n
print("Discounted Amount:",int(discount_amount))