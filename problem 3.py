c=600851475143
i=1
while i<=c:
    if c%i==0:
        a=1
        count=0
        while a<=i:
            b=i%a
            if b==0:
                count=count+1
            a=a+1
        if count==2:
            print(i)

    i=i+1


##c=600851475143
##primelist=[]
##for i in range(2,c):
##    if c%i==0: #i is a factor of c
##        count=0
##        j=2
##        while j<= i**0.5: 
##            if i%j==0:
##                count=+1
##        if count==0: #then i is a prime factor
##            primelist.append(i)
##print(primelist)
##        
##        
