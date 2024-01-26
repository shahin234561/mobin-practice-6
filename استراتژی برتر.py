a , b= map(int,input('').split(' '))




count = 0
if a <= b :
    for num in range(a,b+1):
        if num > 1:
            for i in range(2,num):
             if num % i == 0:
                break
            else:
               count += 1
        
    print(f'main order - amount: {count}')
else:
    for num in range(b,a+1):
        if num > 1:
            for i in range(2,num):
                if num % i == 0:
                    break
                count += 1

    print(f'reverse order - amount: {count}')

                      



   

        
            