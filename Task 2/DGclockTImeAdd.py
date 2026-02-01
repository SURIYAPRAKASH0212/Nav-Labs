h=int(input("Hour: "))
m=int(input("Minute: "))
x=int(input("Extra Minutes or Hour: "))
newh=x//60
h=h+newh
x=x-(newh*60)
newm=x%60
m=m+newm
h=h+(m//60)
m = m % 60
h=h%24
print(h,m)