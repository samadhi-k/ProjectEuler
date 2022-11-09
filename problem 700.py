n = 1
x = 1504170715041707 % 4503599627370517
eularcoin = [x]
while True:
    x = 1504170715041707 * n % 4503599627370517
    if x < eularcoin[-1]:
        eularcoin.append(x)
        print(x)
    if x == 0:
        break
    n += 3
s: int = sum(eularcoin)
print(s)
