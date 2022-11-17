test=int(input())
l1=[]
tt=[]
l2=[]
for i in range(test):
    x=int(input())
    y=input()
    l1.append(x)
    tt=y.split()
    l2.append(tt)

j=0
for i in range(test):
    one=l2[i][l1[i]-1]
    if one!='0':
        two=l2[i][int(one)-1]
        if two!='0':
            three=l2[i][int(two)-1]
            if three=='0':
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")
