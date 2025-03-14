import json
y=input("enter json like format:")
a=input("enter string:")
x=json.loads(y)
print(x[a])