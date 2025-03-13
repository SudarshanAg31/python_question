x=input("enter string_1_:")
y=input("enter string_2_:")
x=x.split()
y=y.split()
z=[]
for i in x:
    i=int(i)
    for j in y:
        j=int(j)
        if i==j:
            z.append(j)
        else:
            pass
a=[]
for i in z:
    if i in a:
        pass
    else:
        a.append(i)
a=tuple(a)
#only for same output
if len(a)==1:
    print(f"({a[0]})")
else:
    print(a)
