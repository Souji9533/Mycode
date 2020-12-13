s=input().split()
n=s[0]
l=[]
n1=int(s[1])

for i in n:
   l=list(combinations(i,n))
l=list(map(list,l))
res=[''.join(el) for el in l]
for a in res:
    print(a)