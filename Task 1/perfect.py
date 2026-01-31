number = int(input("Enter a number: "))
perfect = 0
for i in range(1, number):
    if number % i == 0:
        perfect += i
if perfect == number:
    print(f"{number} is a perfect number.") 
else:
    print(f"{number} is not a perfect number.")