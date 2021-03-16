import sys
sys.setrecursionlimit(10**8) 

def no_omlets(n,e,h,b,c): #WHAT COULD BE MINIMUM ORDER IF NO OMLET IS ORDERED
    
    
    if b<c:
        val = min(n-1,(h-n)//2)
        res =((b-c)*val)+(n*c)
    else:
        val = max(1,n-e)
        res = ((b-c)*val)+(n*c)
    
    
    return res

def no_milkshake(n,e,h,a,c):# 2WHAT COULD BE MINIMUM ORDER IF NO MILKSHAKE IS ORDERED
    
    if a-c<0:
        val = min(n-1,e-n)
        res = (((a-c)*val)+(n*c))
    else:
        val= max(1,n-h)
        res =(((a-c)*val)+(n*c))
    
    return res

def no_cake(n,e,h,a,b):  #WHAT COULD BE MINIMUM ORDER IF NO CAKE IS ORDER #3
    
     
    if a<b:
        val = min(n-1,e//2)
        res = ((a-b)*val)+(n*b)
    else:
        val= max(1,((3*n)-h+2)//3)
        res =((a-b)*val)+(n*b)
        
    
    return res

def college(n,e,h,a,b,c):  #ACTUAL FUNCTION THAT IS IMPLETMENTIING THE ALGORITHEM
    if n<1:
        return 0

    res = 10**14

    if 2*n<= e: # only by omlets
        res = min(res,n*a)

    if n<=e and n<= h: #only by cake 
        res = min(res,n*c)

    if n*3 <=h: #by milkshake
        res = min(res,n*b)


    if (h-n)//2 >=1 and (h-n)//2 >=n-e:
        omlet = no_omlets(n,e,h,b,c)
        if omlet >0 :
            res = min(res,omlet)
        
    
    if((e-n)>=1 and (e-n)>= n-h):
        milks= no_milkshake(n,e,h,a,c)
        if milks >0 :
            res = min(res,milks)
        
    
    if e//2>=1 and e//2>=((3*n)-h+2)//3:
        caked = no_cake(n,e,h,a,b)
        if caked >0 :
            res = min(res,caked)


    if(e>=3 and h>=4 and n>=3):
        res= min(res,a+b+c+college(n-3,e-3,h-4,a,b,c))

    return res


def coll(n,e,h,a,b,c): # FIRST FUNCTION TO DEAL WITH INPUTS
    
    res = college(n,e,h,a,b,c)

    if res == 10**14:
        return -1
    return res


T = int(input()) # TAKES THE INPUT FOR NUMBER OF TEST CASES

for _ in range(T): #LOOP FOR EACH AND EVERY TEST CASE 
    x = input()
    x = x.split(" ")
    
    N = int(x[0])
    E = int(x[1])
    H = int(x[2])
    A = int(x[3])
    B = int(x[4])
    C = int(x[5])
    
    print(int(coll(N,E,H,A,B,C)))
