x=int(input("enter number:"))
my_dic={}
my_dic_len={}
for i in range(x):
    emp_id,emp_name=input("").split(maxsplit=1)
    emp_id=int(emp_id)
    my_dic[emp_id]=emp_name
    my_dic_len[emp_id]=len(emp_name)
    
print(my_dic)
print(my_dic_len)
