balance = int(input("Enter a balance amount: "))
amount = int(input("Enter an amount to withdraw: "))
if amount % 100 != 0:
    print("The amount must be in multiples of 100.")
elif amount > balance:
    print("Insufficient balance.")
else:
    balance -= amount
    if balance < 500:
        print("Warning: Your balance is below the minimum required balance of 500.")
    else:
        print(f"Success! Your new balance is: {balance}")