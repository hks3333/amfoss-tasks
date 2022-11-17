t=int(input())
l=[]
n=[]
for i in range(t):
    p=int(input())
    n.append(p)
    q=input()
    k=q.split()
    l.append(k)
for i in range(len(n)):
    count0=0
    mana=0
    count0+=l[i].count('0')
    if count0==0:
        for j in l[i]:
            if l[i].count(j)>=2:
                mana=n[i]
                break
        else:
            mana=n[i]+1
    else:
        mana=n[i]-count0
    print(mana)
    
    
    
