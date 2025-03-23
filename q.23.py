x=list(map(int,input().split()))
x.sort()
y=max(x)
while y in x :
    x.remove(y)
if x ==[]:
    print("no")
else:
    z=max(x)
    print(z)
