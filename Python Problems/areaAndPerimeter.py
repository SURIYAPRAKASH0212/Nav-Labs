import math
shape=input("Enter the shape((R)rectangle/(C)circle): ")
if shape=="Rectangle" or shape=="rectangle" or shape=="R" or shape=="RECTANGLE" or shape=="r":
    length=float(input("Enter the Length of the Rectangle: "))
    breadth=float(input("Enter the Breadth of the Rectangle: "))
    area=length*breadth
    perimeter=2*(length+breadth)
    print(f"Area: {round(area,2)}\nPerimeter: {round(perimeter,2)}")
elif shape=="Circle" or shape=="Circle" or shape=="C" or shape=="CIRCLE" or shape=="c":
    radius=float(input("Enter the Radius of the Circle: "))
    area=math.pi*radius**2
    circumference=2*math.pi*radius
    print(f"Area: {round(area,2)}\nCircumference: {round(circumference,2)}")
else:
    print("Invalid Input or Check Spelling")