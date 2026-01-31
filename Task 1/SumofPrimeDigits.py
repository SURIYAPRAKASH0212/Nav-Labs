number = int(input("Enter a number: "))
digit_sum = 0
while number > 0:
    digit = number % 10
    isprime = True
    if digit < 2:
        isprime = False
    else:
        for i in range(2, int(digit**0.5) + 1):
            if digit % i == 0:
                isprime = False
                break
    if isprime:
        digit_sum += digit
    number //= 10
print(f"The sum of the prime digits is: {digit_sum}")