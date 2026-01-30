number = int(input("Enter a number: "))
second_largest = -1
largest = -1
while number > 0:
    digit = number % 10
    if digit > largest:
        second_largest = largest
        largest = digit
    elif digit > second_largest and digit != largest:
        second_largest = digit
    number //= 10
print(f"The second largest digit is: {second_largest}")