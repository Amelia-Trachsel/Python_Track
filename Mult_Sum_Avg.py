for i in range (1,10):
    if i%2:
        print i
    else:
        pass
for j in range (5, 100):
    if j%5:
        pass
    else:
        print j
a = [1,2,5,10,255,3]

z = 0
for k in a:
    z += k 

y = z/len(a)
print z 
print y
    