n=int(input())
si=input()
temp=[]
temp=si.split()
l,l1,l2,l3=[],[],[],[]
cars=0
for i in temp:
    l.append(int(i))
    if int(i)==1:
        l1.append(int(i))
    elif int(i)==2:
        l2.append(int(i))
    elif int(i)==3:
        l3.append(int(i))
    else:
        cars+=1
        l.remove(int(i))


while l!=[]:
    if l[0]==3:
        l3.pop(0)
        l.pop(0)
        if l1!=[]:
            cars+=1
            l1.pop(0)
            l.remove(1)
        else:
            cars+=1
    elif l[0]==2:
        l2.pop(0)
        l.pop(0)
        if l2!=[]:
            l2.pop(0)
            cars+=1
            l.remove(2)
        else:
            if l1!=[]:
                if len(l1)>=2:
                    l1.pop(0)
                    l1.pop(0)
                    cars+=1
                    l.remove(1)
                    l.remove(1)
                else:
                    l1.pop(0)
                    cars+=1
                    l.remove(1)
            else:
                cars+=1
    elif l[0]==1:
        l1.pop(0)
        l.pop(0)
        if l3!=[]:
            l3.pop(0)
            l.remove(3)
            cars+=1
        elif l2!=[]:
            l2.pop(0)
            l.remove(2)
            if l1!=[]:
                l1.pop(0)
                l.remove(1)
                cars+=1
            else:
                cars+=1
        elif l1!=[]:
            if len(l1)>=3:
                l1.pop(0)
                l1.pop(0)
                l1.pop(0)
                l.remove(1)
                l.remove(1)
                l.remove(1)
                cars+=1
            elif len(l1)==2:
                l1.pop(0)
                l1.pop(0)
                l.remove(1)
                l.remove(1)
                cars+=1
            elif len(l1)==1:
                l1.pop(0)
                l.remove(1)
                cars+=1
        else:
            cars+=1

print(cars)


