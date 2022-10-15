from itertools import combinations
x=[int(i) for i in input().split(' ')]
l=[int(i) for i in input().split(' ')]
c=list(combinations(l,x[1]))
t=0
for i in c:
    k=1
    for j in i:
        k=k*j
    t=t+k
t=t%x[0]
for m in range(1,x[0]):
    if ((t*m)%x[0]==1:
        b=m
    b=k%(10**9+7)
    print(b)
