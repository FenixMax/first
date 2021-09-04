n=8
x=[]
y=[]
g=22
while g<n:
    x1=int(input("введите координату на доске(цифра от 1 до 8)"))
    y1=input("введите буквенную координату(заглавная латинская буква от A до H")
    if y1=="A":
        y1=1
    elif y1=="B":
        y1=2
    elif y1=="C":
        y1=3
    elif y1=="D":
        y1=4
    elif y1=="E":
        y1=5
    elif y1=="F":
        y1=6
    elif y1=="G":
        y1=7
    elif y1=="H":
        y1=8
    x.append(x1)
    y.append(y1)
    g+=1
a=[]
b=[]
for i in range(n):
    for j in range(i+1,n):
        if x[i]==x[j] or y[i]==y[j] or abs(x[i]-x[j])==abs(y[i]-y[j]):
            print("YES")
        else:
            print("NO")
