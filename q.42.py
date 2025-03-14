x=int(input("enter number:"))
my_dic={}
z=int(input("threshold:"))
for i in range(x):
    string,num=input("enter string & num:").split(maxsplit=1)
    num=int(num)
    my_dic[string]=num
my_new_dic={}
for i,j in my_dic.items():
    if j>z:
        my_new_dic[i]=j
print(my_new_dic)