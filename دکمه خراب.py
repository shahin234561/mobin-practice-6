a=int(input(''))
b=int(input(''))
c=int(input(''))
a=bin(a)
b=bin(b)
d=bin(c)
# print(a)
# print(b)
# print(d)
a=a.replace('0b','')
b=b.replace('0b','')
d=d.replace('0b','')

x = 0
if len(a)<len(b):
    number_of_zeros_to_add = len(b) - len(a)
    a = a.zfill(len(a) + number_of_zeros_to_add)
elif len(a)>len(b):
    number_of_zeros_to_add = len(a) - len(b)
    b = b.zfill(len(b) + number_of_zeros_to_add)

carry = 0
answer = ''
i = len(a) - 1
while (i >= 0):
    if a[i] == '0' and b[i] == '0':
        if carry == 0:
            answer = '0' + answer 
        else:
            answer = '1' + answer
            carry = 0
        if i == 0 and carry==1:
                answer = '1' + answer
    elif a[i] == '1' and b[i] == '0':
        if carry == 0:
            answer = '1' + answer
            
        else:
            answer = '0' + answer
            carry = 1
        if i == 0 and carry==1:
                answer = '1' + answer    
    elif a[i] == '0' and b[i] == '1':
        if carry == 0:
            answer = '1' + answer
        else:
            answer = '0' + answer
            carry = 1
        if i == 0 and carry==1:
                answer = '1' + answer  
    elif a[i] == '1' and b[i] == '1':
        if carry == 0:
            answer = '0' + answer
            carry = 1
        else:
            answer = '1' + answer
            carry = 1
        if i == 0 and carry==1:
                answer = '1' + answer
    i = i -1

    



# print(answer)




number=int(answer,2)


if number == c:
    print(number)
    print('YES')
else:
    print(number)
    print('NO')

