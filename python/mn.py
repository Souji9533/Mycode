# from collections import defaultdict
# d = defaultdict(list)
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#     print(i)
# n=intput()
# x=input()
# for i in range(x):
#     print(i)
# from collections import defaultdict
# d = defaultdict(list)
# list1=[]
# Enter your code here. Read input from STDIN. Print output to
from collections import defaultdict
d = defaultdict(list)
list1=[]
n, m = map(int,input().split())

for i in range(n):
    d[input()].append(i+1) 

for i in range(0,m):
    list1=list1+[input()]  

for i in list1: 
    if i in d:
        print(" ".join( map(str,d[i])))
    else:
        print -1

