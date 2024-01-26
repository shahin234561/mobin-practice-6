a = int(input(''))
b = int(input(''))
A = bin(a)
B = bin(b)

A=A.replace('0b','')
B=B.replace('0b','')
if len(A) <= 32:
    number_of_zeros_to_add = 32 - len(A)
    c = A.zfill(len(A) + number_of_zeros_to_add)

if len(B) <= 32:
    number_of_zeros_to_add = 32 - len(B)
    d = B.zfill(len(B) + number_of_zeros_to_add)   
    



x = d + c

x=x[::-1]

list=[]
k = int(input(''))
while k != 0 :
    g=int(input(''))
    k=k-1
    list.append(g)

    
for i in list:
    if x[i]=='1':
        print('yes')
    else:
        print('no')
       






