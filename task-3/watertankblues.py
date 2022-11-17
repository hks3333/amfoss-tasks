def duh(l):
    c=0
    ln=len(l)
    for i in range(ln):
        if l[i]!=0:
            ls=l[i:ln-1]
            break
        else:
            continue
    for j in range(len(ls)):
        if ls[j]==0:
            c+=1
        else:
            c+=ls[j]
    return c


storagefac=int(input())
no_tanks=[]
wateramount=[]
for i in range(storagefac):
    b=int(input())
    no_tanks.append(b)
    n=(input())
    k=n.split()
    l=[]
    for p in range(len(k)):
        l.append(int(k[p]))
    wateramount.append(l)
for m in wateramount:
    print(duh(m))




    
