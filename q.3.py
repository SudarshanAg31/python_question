x=float(input())
y=float(input())
z=input()
if z=="+":
    print(x+y)
elif z=="-":
    print(x-y)
elif z=="*":
    print(x*y)  
elif z=="/":
    if y!=0:
        print(f"{x/y:.1f}")
    else:
        print("Error: Division by zero")  