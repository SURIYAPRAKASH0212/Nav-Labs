a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))
while b:
    a, b = b, a % b
print(f"The HCF (GCD) of the two numbers is: {a}")