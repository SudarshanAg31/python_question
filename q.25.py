x=input("enter number:")
x=x.split()
z=[]
y=int(input("enter value:"))
for i in range(len(x)-y,len(x)):
    z.append(x[i])
for i in range(0,len(x)-y):
    z.append(x[i])
print(z)