x=input("enter number:")
x=x.split()
count=0
y=0
my_dic={"Math":0,"Science":0,"English":0}
for i,j in my_dic.items():
    j=int(x[count])
    y+=j
    my_dic.update({i:j})
    count+=1
print(my_dic)
print(f"{y/3:.2f}")
    