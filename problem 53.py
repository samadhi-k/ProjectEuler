import math


def comb(n, r):
    x = math.factorial(n)
    y = math.factorial(r)
    z = math.factorial(n - r)
    return x / (y * z)


##def multi(n,r):
##    if n==r:
##        return 1
##    else:
##        p=n* multi(n-1,r)
count = 0
for i in range(23, 101):
    for j in range(1, i):
        y = comb(i, j)
        if y > 1000000:
            count += 1
print(count)
