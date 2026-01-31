n=int(input("Enter n: "))
oddDcount=0
evenDcount=0
while n>0:
    digit=n%10
    if digit%2==0:
        evenDcount+=1
    else:
        oddDcount+=1
    n//=10
print("Even Digits :",evenDcount)
print("Odd Digits :",oddDcount)