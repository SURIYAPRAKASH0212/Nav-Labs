number = int(input("Enter a number: "))
num = number
d_sum = 0
while number > 0:
    d_sum += number % 10
    number //= 10
if (num%10)%2 == 0 and d_sum%3 == 0:
    print(f"The number {num} is a digit security number.")