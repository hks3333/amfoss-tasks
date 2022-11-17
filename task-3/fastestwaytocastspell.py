n=input()
nos=[]
nos=n.split()
l=[]
for i in range(int(nos[1])):
    k=[]
    st=input()
    k=st.split()
    l.append(k)
spell=input()
spellist=[]
spellist=spell.split()
finalist=[]
for j in spellist:
    for m in l:
        if m[0]==j:
            if len(m[0])<=len(m[1]):
                finalist.append(m[0])
                break
            else:
                finalist.append(m[1])
                break
        else:
            continue
print(' '.join(finalist))
    
