
number = int(input("Enter a number: "))
digit = int(input("Enter the digit to count: "))
count = 0
while number > 0:
    current_digit = number % 10
    if current_digit == digit:
        count += 1
    number //= 10
print(f"The digit {digit} occurs {count} times.")