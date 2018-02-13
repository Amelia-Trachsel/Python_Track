l = ['magical unicorns',19,'hello',98.98,'world']
j = [2,3,1,7,4,12]
k = ['magical','unicorns']
NewStr = []
RunSum = 0
Master = [l,j,k]
for i in range (0,len(Master)):
    for m in range (0, len(Master[i])):
        if isinstance(Master[i][m], str):
            NewStr += Master[i][m]
        elif isinstance(Master[i][m], int):
            RunSum += Master[i][m]
print NewStr
print RunSum
if all(isinstance(i,str) for i in l):
    print "String!"
elif all(isinstance(i,int) for i in l):
    print "Integer!"
else :
    print "Mixed!"
if all(isinstance(i,str) for i in j):
    print "String!"
elif all(isinstance(i,int) for i in j):
    print "Integer!"
else :
    print "Mixed!"
if all(isinstance(i,str) for i in k):
    print "String!"
elif all(isinstance(i,int) for i in k):
    print "Integer!"
else :
    print "Mixed!"


