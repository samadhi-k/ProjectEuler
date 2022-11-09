f1=1
f2=1
c=2
while True:
    f3=f1+f2
    f1,f2=f2,f3
    x=str(f3)
    c=c+1
    if len(x)==1000:
        print(c)
        break
