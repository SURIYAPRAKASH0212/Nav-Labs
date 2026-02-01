length=int(input("length:"))
width=int(input("width:"))
height=int(input("height:"))
if length and width and height > 0 and length+width+height<=150:
    print("Accepted")
else:
    print("Rejected")