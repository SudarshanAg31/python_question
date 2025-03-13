x=input("enter string:")
if len(x)%2==0:
    y=set()
    for i in x:
        y.add(i)
    if len(y)==len(x)/2:
        print("True")
    else:
        print("Flase")
else:
    y=set()
    for i in x:
        y.add(i)
    if len(y)==(len(x)//2)+1:
        print("True")
    else:
        print("Flase")
