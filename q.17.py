q=input("enter string & sub-string:")
q=q.split()
x=q[0]
n=q[1]
y=len(n)
count=0
for i in range(0,len(x)-y+1):
    if x[i:i+y]==n:
        count+=1
    else:
        pass
print(count)