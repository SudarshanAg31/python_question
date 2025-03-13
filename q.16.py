x=int(input("enter number:"))
if (x%4==0 or x%400==0) and (x%100!=0):
    print("LY")
else:
    print("NLY")