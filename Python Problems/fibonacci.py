number = int(input("Enter a number: "))
first = 0
last = 1
for i in range(number):
    print(first)
    next = first + last
    first = last
    last = next