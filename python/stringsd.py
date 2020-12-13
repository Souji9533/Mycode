from itertools import combinations_with_replacement
s=input().split()
n=s[0]
n1= int(s[1])
print(list(combinations_with_replacement(n,n1)))
#print(per)
l=list(combinations_with_replacement(n,n1))
l=list(map(list,l))
print(l)
res = [''.join(ele) for ele in l]
res.sort() 
print(res)
for i in res:
    print(i)