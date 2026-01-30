p=int(input("Enter Principal Amount: "))
r=int(input("Enter Rate of Interest: "))
t=int(input("Enter Time Period: "))
compound_interest=p*(1+r/100)**t-p
print("Calculated Simple Interest: ",compound_interest)