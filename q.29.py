x=input("enter number:")
x=x.split()
x=tuple(x)
print(x)
sum=0
for i in x:
    sum+=int(i)
z=sum/len(x)
print(f"avrage:{z:.2f}")