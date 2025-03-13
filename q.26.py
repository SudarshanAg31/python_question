x=input("")
y=int(input(""))
x=x.split()
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if int(x[i])+int(x[j])==y:
            print(i,j)
            exit()