a=11
s=17
while a<2000000:
    b=3
    while True:
        if a%b==0:
            break
        b=b+2
        
    if b==a:
        s=s+a
        print(a)
    a=a+2
print(s)

## marked=[0]*2000000
## value=3
## s=2
## while value< 2000000:
##     if marked[value]==0:
##         s+=value
##         i=value
##         while i<2000000:
##             marked[i]=1
##             i+=value
##     value+=2
## print(s)
