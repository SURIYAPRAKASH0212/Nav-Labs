n = int(input("Enter a natural number: "))
for i in range(2, n+1):
    isprime = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            isprime = False
            break
    if isprime:
        print(i)