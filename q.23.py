x=input("enter number:")
x=x.split(",")
y=[]
for i in x:
    try:
        y.append(int(i)) 
    except ValueError:
        pass
y.sort()
max=y[-1] 
max=int(max)
for i in reversed(range(0,len(y))):
    if max>y[i]:
        print(y[i])
        exit()
    else:
        pass
print("no second highest") 
