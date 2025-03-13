x=input("enter words:")
x=x.split(",")
count=0
y=input("enter substring:")
for i in x:
    if i[:len(y)]==y:
        count+=1
    else:
        pass
if count==0:
    print("There are no strings")
else:
    print(count)
