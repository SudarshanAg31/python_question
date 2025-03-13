a=input("enter string & sub-string:")
a=a.split()
x=a[0]
y=a[1]
b=[]
c=[]
for i in x:
    b.append(i)
b.sort()
for i in y:
    c.append(i)
c.sort()
if b==c:
    print("True")
else:
    print("False")