n=int(input("Enter n: "))
num=n
reversedNum=0
while n>0:
    digits=n%10
    reversedNum=reversedNum*10+digits
    n//=10
if num==reversedNum:
    print("Palindrome")
else:
    print("Not A Plaindrome")