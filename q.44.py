#hacker rank
n=int(input())
dic={}
for i in range(n):
    x=input().split()
    q=x[0]
    x.remove(q)
    dic[q]=list(map(float,x))
z=input("")
sum=0
for i in dic[z]:
    sum+=i
print(f"{sum/3:.2f}")