x=input()
count=0
countt=0
counttt=0
for i in x:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u"or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        count+=1
    elif i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9" or i=="0":
        counttt+=1
    else:
        countt+=1
print(count)
print(countt)
print(counttt)
