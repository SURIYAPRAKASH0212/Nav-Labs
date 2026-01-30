n=int(input("Enter n: "))
num=n
digits=0
while n>0:
    digits+=1
    n//=10
n=num
armstrong=0
for i in range(digits):
    armstrong+=(num%10)**digits
    num//=10
if armstrong==n:
    print(f"{n} is a Armstrong NUmber")
else:
    print(f"{n} is Not a Armstrong Number")