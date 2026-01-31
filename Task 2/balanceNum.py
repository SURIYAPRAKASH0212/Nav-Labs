number = int(input("Enter a number: "))
sum1 = 0
sum2 = 0
temp = number
length = len(str(number))
number = str(number)
for i in range(length//2):
    sum1 += int(number[-(1+i)])
    sum2 += int(number[i]) 
print("The number is balanced" if sum1 == sum2 else "The number is not balanced")
print(f"Left sum: {sum1}, Right sum: {sum2}")