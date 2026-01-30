n= int(input("Enter n: "))
i = 2
isprime=True
while i<n:
    if n%i==0:
        isprime=False
        break
    i+=1
if isprime and n > 1:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")