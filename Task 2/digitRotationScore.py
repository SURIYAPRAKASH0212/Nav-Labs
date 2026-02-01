n=int(input("Enter a Number: "))
a=n
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n//=10
ans=reverse+a
print("Score:",ans)