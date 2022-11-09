m=10000
for a in range(100,1000):
    for b in range (100,1000):
        c=a*b
        d=str(c)
        e=d[::-1]
        if d==e and c>m:
            m=c
print(m)

