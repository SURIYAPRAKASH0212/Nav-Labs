number = int(input("Enter a number: "))
first = 0
last = 1
for i in range(number):
    print(first,end=" ")
    next = first + last
    first = last
    last = next