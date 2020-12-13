# s='qA2'
# for i in s:
#     print(s.isalnum())
#     print(s.isalpha())
#     print(s.isdigit())
#     print(s.islower())  
#     print(s.isupper())
# Enter your code here. Read input from STDIN. Print output to STDOUT
# import itertools
# s='hack'
# for i in 'hask':
#     print(itertools.permutations(s))
from itertools import permutations
perms =[p for p in permutations(list('hack'),2)]
print(perms)
perms=list(map(list,perms))
print(perms)
#print("\n".join(perms))
res = [''.join(ele) for ele in perms] 
print(res)
for i in res:
    print(i)    