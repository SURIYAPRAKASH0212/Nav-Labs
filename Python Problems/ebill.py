units = int(input("Enter Units: "))
if units<=100:
    bill=0
elif units>100 and units<=200:
    bill=(units-100)*2.25
elif units>200 and units<250:
    bill=(100*2.25)+((units-200)*4.80)
print("Bill: ",bill)