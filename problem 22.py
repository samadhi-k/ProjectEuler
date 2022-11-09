a= open('C:\\Users\Samadhi Kariyawasam\Documents\p022_names.txt')
names=a.read().strip('"').split('","')
names.sort()
names_sum=[]
letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(names)):
    name_sum=0
    for j in names[i]:
        name_sum+=(letters.index(j)+1)
    name_sum*=(i+1)
    names_sum.append(name_sum)
print(sum(names_sum))

