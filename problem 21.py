amicale=[]
for i in range(1,10001):
    if i not in amicale:
        divisor=[]
        for j in range(1,i):
            if i%j==0:
                divisor.append(j)
        a=sum(divisor)
    divisor1=[]
    if a not in amicale:
        for k in range(1,a):
            if a%k==0:
                divisor1.append(k)
        b=sum(divisor1)
    if b==i and a not in amicale and b not in amicale and i!=a and a!=b :
        amicale.append(a)
        amicale.append(b)
print(sum(amicale))            
    
