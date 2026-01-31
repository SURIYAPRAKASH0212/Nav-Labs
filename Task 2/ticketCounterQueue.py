age =int(input("Enter Age: "))
ticket=200
if age<0:
    print("Invalid Age")
elif age<5:
    print("Free Ticket")
elif age<=12:
    print("Discounted Ticket:",ticket-(ticket/2))
elif age<60:
    print("Full Ticket:",ticket)
else:
    print("Discounted Ticket:",ticket-(ticket*0.3))