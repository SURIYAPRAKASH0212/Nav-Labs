a = int(input("Enter the base number: "))
b = int(input("Enter the exponent number: "))
result = 1
for i in range(b):
    result *= a
print(f"{a} raised to the power of {b} is: {result}")