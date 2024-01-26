number1=int(input(''))
number2=int(input(''))
number3=int(input(''))
number1=bin(number1)
number2=bin(number2)
number3=bin(number3)

number1=number1.replace('0b','')
number2=number2.replace('0b','')
number3=number3.replace('0b','')

x = 0
if len(number1)<len(number2):
    number_of_zeros_to_add = len(number2) - len(number1)
    number1 = number1.zfill(len(number1) + number_of_zeros_to_add)
elif len(number1)>len(number2):
    number_of_zeros_to_add = len(number1) - len(number2)
    number2 = number2.zfill(len(number2) + number_of_zeros_to_add)

carry = 0
answer = ''
i = len(number1) - 1
while (i >= 0):
    if number1[i] == '0' and number2[i] == '0':
        if carry == 0:
            answer = '0' + answer 
        else:
            answer = '1' + answer
            carry = 0
        if i == 0 and carry==1:
                answer = '1' + answer
    elif number1[i] == '1' and number2[i] == '0':
        if carry == 0:
            answer = '1' + answer
            
        else:
            answer = '0' + answer
            carry = 1
        if i == 0 and carry==1:
                answer = '1' + answer    
    elif number1[i] == '0' and number2[i] == '1':
        if carry == 0:
            answer = '1' + answer
        else:
            answer = '0' + answer
            carry = 1
        if i == 0 and carry==1:
                answer = '1' + answer  
    elif number1[i] == '1' and number2[i] == '1':
        if carry == 0:
            answer = '0' + answer
            carry = 1
        else:
            answer = '1' + answer
            carry = 1
        if i == 0 and carry==1:
                answer = '1' + answer
    i = i -1

    
number=int(answer,2)


if number == number3:
    print(number)
    print('YES')

print(number)
print('NO')

