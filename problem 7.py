a=2
count=0
while True:
    b=2
    c=0
    while b<=a:
        if a%b==0:
            c=c+1
        b=b+1
    if c==1:
        count=count+1
    if count==10001:
        print(a)
        break
    a=a+1
 
