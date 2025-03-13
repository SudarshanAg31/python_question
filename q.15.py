y=input("enter number:")
x=y.split()
for i in x:
    i=int(i)
    if i>0 and i<=26:    
        i=i+64
        if i>40 and i<91:
            print(chr(i),end="")
    else:
        i=i+70    
        if i>96 and i<123:
            print(chr(i),end="")