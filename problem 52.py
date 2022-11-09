x=125874
def multi(n):
    l=[n,2*n,3*n,4*n,5*n,6*n]
    return l
while True:
    numbers=multi(x)
    right=[]
    for i in numbers:
        j=list(str(i))
        k=sorted(j)
        if right==[] or k in right:
            right.append(k)
        else:
            break
    if len(right)==6:
        print(x)
        break
    x+=1
