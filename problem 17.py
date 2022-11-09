digit1 = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
digit2_1 = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
digit2_2 = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
digit2_3 = [0, 6, 6, 5, 5, 5, 7, 6, 6]
lc = 0
for i in range(1, 1001):
    j = list(str(i))
    k = list(map(int, j))
    if len(k) == 1:
        lc += digit1[k[0]]
    if len(k) == 2:
        if k[0] == 1:
            lc += digit2_1[k[1]]
        else:
            lc += digit2_3[k[0] - 1]
            lc += digit1[k[1]]
    if len(k) == 3:
        lc += digit1[k[0]]
        lc += 10
        if k[1] == 0 and k[2] == 0:
            lc = lc - 3
        if k[1] == 1:
            lc += digit2_1[k[2]]
        else:
            lc += digit2_2[k[1]]
            lc += digit1[k[2]]
    if len(k) == 4:
        lc += 11
print(lc)
