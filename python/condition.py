p=int(input())
q=int(input())
result=0
l=[]
for i in range(p,q+1):
    a=list(map(int,list(str(i*i))))
    if len(a)==2:
        if sum(a)==i:
            print(i)
    elif len(a)==3:
        pass
    elif len(a)==4:
        res=[ ''.join((str(a[x]),str(a[x+1]))) for x in range(len(a)-1)]
        res=list(map(int,res))
        #print(res)
        if sum(res)==i:
             print(sum(res))
   
    
                
            
    



    # if len(a)<6:
    #     #print("true")
    #     for k in a:
    #         l.append(k)
    # for j in l:
    #     result=result+int(j)
    #     if result==i:
    #         print(i)
        #     result=result+int(a[k])
        #
        #     
