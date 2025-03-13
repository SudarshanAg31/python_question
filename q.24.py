x = input("enter number:")  
x=x.split()
y = []  
for i in x:  
    y.append(i)  
z = int(y[0])  
for i in range(1, len(y)):  
    a = int(y[i-1])    
    if a + 1 != int(y[i]):  
        print(a + 1)  
        exit()  
print("no missing number found")