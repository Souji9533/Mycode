# from itertools import product
# s= input().split()
# s1=s[0]
# s2=s[1]
# l=list(product(s1,s2))
# for i in l:
#     print(i, end=" ")


from itertools import product
s=input()
s1=input()
l=list(product(s,s1))
for i in l:
    print(i, end =" ")

    # Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *
io = input()
for i,j in groupby(map(int,list(io))):
    print(tuple([len(list(j)), i]) ,end = " ")a
