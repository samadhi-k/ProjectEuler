def collartz(num,a):
    if num==1:
        a.append(num)
        return a 
    elif num%2==0:
        a.append(num)
        return collartz(num/2,a)
    elif num%2==1:
        a.append(num)
        return collartz(3*num+1,a)
large=0
m=0
for i in range(13,1000001):
    print(i)
    x=[]
    y=collartz(i,x)
    if len(y)>large:
        large=len(y)
        m=i
print(m)
    
