list=[1,1]


a=int(input(''))
if a==1+0:
    print(1)
elif a==1+1:
    print(1)
    print(f'{list[0]} {list[1]}')
else:
    b=[]
    i=1
    j=0
    print(1)
    print(f'{list[0]} {list[1]}')
    b.append(1)

    while a>1+1: 
        while i<len(list):
            while j<len(list)-1:
                b.append(list[j]+list[j+1])
                j+=1
            i+=1
            j=0        
        a-=1
        b.append(1)
        list=b

        for item in b:
            print(item,end=' ')       
        b=[] 
        b.append(1) 
        print()