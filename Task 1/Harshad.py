number = int(input("Enter a number: "))
num = number
sum_of_digits = 0
while number > 0:
    sum_of_digits += number % 10
    number //= 10
if num % sum_of_digits == 0:
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")