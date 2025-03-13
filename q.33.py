x=input("enter string_1_:")
y=input("enter string_2_:")
x=x.split()
y=y.split()
z=x+y
v=[]
for i in z:
    if i in v:
        pass
    else:
        v.append(i)
v=tuple(v)
print(v)