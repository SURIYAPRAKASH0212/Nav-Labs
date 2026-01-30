number = int(input("Enter a number: "))
count = 0
for i in range(1, number):
    if number % i == 0:
        count += 1
print(f"The number of factors of {number} is: {count}")