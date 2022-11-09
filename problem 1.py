total = 0
i = 1
while i < 1000:
    if i % 3 == 0:
        total = total + i
    elif i % 5 == 0:
        total = total + i
    i = i + 1
print(total)
