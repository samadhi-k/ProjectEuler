x=0
y=0
while y<1000:
    for x in range(1000):
        a=x**2+y**2
        b=2*x*y
        c=x**2-y**2
        if a+b+c == 1000:
            print(a*b*c)
           
    y=y+1
