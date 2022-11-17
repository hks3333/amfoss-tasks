n=input()
l=n.split()
j=int(l[1])
k=int(l[0])
tt=0
if j%k!=0:
    print(-1)
else:
    c=0
    no=j//k
    while no!=1:
        if no%3==0:
            no=no//3
            c+=1
        elif no%2==0:
            no=no//2
            c+=1
        else:
            tt+=1
            print(-1)
            break
    if tt==0:
        print(c)
    
