x=input("enter string:")
y=input("enter name:")
x=x.split()
count=0
for i in x:
    if i==y:
        count+=1
        z=x.index(i)
if count==1:
    print(z)
else:
    print("-1")
        