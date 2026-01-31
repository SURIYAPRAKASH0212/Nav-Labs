a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
x, y = a, b
while y:
    x, y = y, x % y
lcm = (a * b) // x
print(f"The LCM of {a} and {b} is: {lcm}")