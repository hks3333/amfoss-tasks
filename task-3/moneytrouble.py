n=input()
l=[]
for i in n.split():
    l.append(int(i))
if l[0]%2==0:
    c1=0
else:
    c1=1
c2=l[0]//2
if l[0]<l[1]:
    print(-1)
else:
    while (c1+c2)%l[1]!=0:
        c2-=1
        c1+=2
    print(c2+c1)
