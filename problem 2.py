a = 1
b = 2
t = 0
total = 2
while True:
    t = a + b

    if t % 2 == 0:
        total = total + t
    if t > 4000000:
        break
    a = b
    b = t

print(total)
