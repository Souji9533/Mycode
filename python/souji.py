from itertools import permutations
s=input().split()
n=s[0]
l=[]
n1=int(s[1])
l=[i for i in permutations(list(n),n1)]
#per=[a for a in permutations(list(n),n1)]
#per=list(map(list,per))     
l=list(map(list,l))
res = [''.join(ele) for ele in l]
#res1 = [''.join(ele) for ele in per] 
#res2=res+res1
res.sort()
print(res)
for a in res:
    b=a
    if b==a:
         