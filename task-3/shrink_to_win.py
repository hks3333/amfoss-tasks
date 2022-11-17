c=0
def rec(n):
    global c
    j=0
    l=[]
    l[:0]=n
    if len(l)==1:
        return c
    else:
        c+=1
        for i in l:
            j+=int(i)
        return rec(str(j))
    

n=input()
print(rec(n))
