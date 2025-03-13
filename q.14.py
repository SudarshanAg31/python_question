x=int(input("enter side 1:"))
y=int(input("enter side 2:"))
z=int(input("enter side 3:"))
if x==y and y==z:
    print("equilateral triangle")
elif x==y or y==z or z==x:
    print("isosceles triangle")
else:
    print("scalene triangle")