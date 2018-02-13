words = "It's thanksgiving day. It's my birthday too!"
print words.find('day')
words.replace('day','month')

x = [2,54,-2,7,12,98]
print max(x)
print min(x)

y = ["hello", 2,54, -2, 7, 12,98, "world"]
z = []
z.append(y[0])
z.append(y[len(y)-1])
print z 

q = [19, 2,54,-2,7,12,98,32,10,-3,6]
q.sort()
s=len(q)/2
print q
print s
r=[]
t = []

for i in range( 0,s):  
    r.append(q[0])
    q.pop(0)
for j in range (0,s):
    t.append(q[0])
    q.pop(0)
t.insert(0,r)
print t
