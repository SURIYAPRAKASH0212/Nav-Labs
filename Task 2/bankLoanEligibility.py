cgpa=float(input("cgpa:"))
att=int(input("attendance:"))
arr=int(input("arrears:"))
if cgpa>=7.5 and att>=75 and arr==0:
    print("Eligible")
else:
    print("Not Eligible")