mult1 = [1,2,3,4,5,6,7,8,9,10,11,12]
mult2 = [1,2,3,4,5,6,7,8,9,10,11,12]
tab = []
for i in range(0,12):
    for j in range(0,12):
        tab.extend([mult1[i]*mult2[j]])  
key = [1,2,3,4,5,6,7,8,9,10,11,12]
m = 12
n = 0
q = " "
print q, tab[0:12]
for k in range (0, 144, 12): 
    print key[n],tab[k:m]
    n += 1
    m += 12
    