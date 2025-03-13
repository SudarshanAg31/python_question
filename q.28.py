x=int(input("enter number:"))
y=int(input("enter number:"))
z=[]
for i in range(x):
    row=[]
    for j in  range(y):
        a=int(input("enter number:"))
        row.append(a)
    z.append(row)

v=[]
for i in range(x):
    sum_row=0
    for j in range(y):
        sum_row+=z[i][j]
    v.append(sum_row)

for j in range(y):
    sum_col=0
    for i in range(x):
        sum_col+=z[i][j]
    v.append(sum_col)
print(v)