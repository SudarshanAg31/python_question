#find largest odd number in string
#("34686")--->(3)
#("462368")--->(4623)
#("246821")---->(246821)
x=input("enter number:")
count=0
for i in x:
    if int(i)%2==0:
        count+=1
    else:
        break
print(x[0:count+1])