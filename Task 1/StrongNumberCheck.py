number = int(input("Enter a number: "))
num = number
strong = 0
while number > 0:
    digit = number % 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    strong += fact
    number //= 10
if strong == num:
    print(f"{num} is a strong number.")
else:   
    print(f"{num} is not a strong number.")