number1 = int(input(''))
number2 = int(input(''))
binary1 = bin(number1)
binary2 = bin(number2)

binary1=binary1.replace('0b','')
binary2=binary2.replace('0b','')
if len(binary1) <= 32:
    number_of_zeros_to_add = 32 - len(binary1)
    c = binary1.zfill(len(binary1) + number_of_zeros_to_add)

if len(binary2) <= 32:
    number_of_zeros_to_add = 32 - len(binary2)
    d = binary2.zfill(len(number2) + number_of_zeros_to_add)   
    
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
print('no')
       






