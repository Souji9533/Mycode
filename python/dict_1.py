# Enter your code here. Read input from STDIN. Print output to
from collections import defaultdict
d = defaultdict(list)
l1=[]
l2=[]
s,a=list(map(int,input().split()))
for i in range(a):
    a=input()
    l1.append(a)
    for k in range(s):
        b=input()
        l2.append(b)
print(l1)
    
 

        
