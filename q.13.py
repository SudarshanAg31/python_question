n=int(input("enter number:"))
for i in range(1,(n//2)+2):
    for j in range(1,2*i):
        print("*",end="")
    print()
for i in reversed(range(1,(n//2)+1)):
    for j in range(1, 2*i):
        print("*",end="")
    print()     