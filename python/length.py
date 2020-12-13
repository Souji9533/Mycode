
# from itertools import permutations
# # s=input()
# # a=1
# # #per = [p for p in permutations(list(s[0]))]
# # for i in permutations(list(s),a):
# #     a=a+1
# #     per=i
# #     print(per)
# #import itertools
# s=input().split()
# n=s[0]
# a=0
# l=[]
# n1=int(s[1])
# for i in permutations(list(n)):
#     l=[i]
# per=[p for p in permutations(list(n),n1)]
# per =list(map(list,per))
# l =list(map(list,l))

# #print(per)
    
    
#     # value=itertools.permutations(i)
#     # for value in i:
#     #     l=value
    
#     #,for i in permutations(list(n),):
    
# #print(l)
# #l1=[]
# #l1=l+per
# #print(l1)
# #l1=list(map(list,l1))
# print(l)
# #l.sort()
# res1 = [''.join(e) for e in l] 
# print(res1)
# res1.sort()
# print(res1)
# for a in res1:
#     print(*a,sep='\n')
# #print(l)
# res = [''.join(ele) for ele in per] 
# res.sort()
# for a in res:
#     print(a)
from itertools import permutations
s=input().split()
n=s[0]
l=[]
n1=int(s[1])
for i in permutations(list(n)):
    l=i
per=[a for a in permutations(list(n),n1)]
l1=set(per)
l1=list(map(list,l1))     
l=list(map(list,l))
res1 = [''.join(ele) for ele in l] 
res = [''.join(ele) for ele in l1] 
res1.sort()

res.sort()
print(res1)
print(res)
res2=res1+res
for a in res2:
    print(a)