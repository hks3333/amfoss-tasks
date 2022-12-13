def fibo(n):
    x,y,z,arr=1,2,0,[2]
    while True:
        z=0
        z=x+y
        x=y
        y=z
        if z>n:
            break
        if z%2==0:
            arr.append(z)
    return sum(arr)
            


t = int(input())
l=[]
for a0 in range(t):
    n = int(input())
    l.append(fibo(n))
for i in l:
    print(i)
    
