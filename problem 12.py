a=0
i=1
all_prime=[2,3,5,7,11,13,17,19,23,31,37,41,43,47,51]
while True:
    a+=i #a is the triangle number
    factors=[]
    b=a
    while b>1:
        for k in all_prime:
            if b%k==0:
                factors.append(k)
                b=b/k
                break
        else:
            all_prime.append(b)
##        count=0
##        for j in range(2,int(b**0.5)+1):
##            if b%j==0:
##                count+=1
##        if count==0:
##            if b not in all_prime:
##                all_prime.append(b)
##                break
    y=[]
    mul=1
    for l in factors:
        if l not in y:
            c=factors.count(l)
            mul*=(c+1)
            y.append(l)
    if mul>500:
        print(a)
        break
    print(a,mul)
    i+=1
    
##def fact(num,prime):
##    facors=[]
##    if num==1:
##        return factors
##    elif 
