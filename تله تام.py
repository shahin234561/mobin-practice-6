import math

from functools import reduce
tale = input('')


while tale != 'sum' and tale != 'average' and tale != 'lcd'and tale != 'gcd' and tale!= 'min' and tale != 'max':
    print('Invalid command')
    break

else:
    a = []
    n =0
    while n != 'end':
        n = input()
        a.append(n)
    a.remove('end')
    b = 0

    if tale == 'sum':
        for i in a[0:len(a)]:
            b = b + int(i)
        print(b)

    elif tale == 'average':
        for i in a[0:len(a)]:
            
            b = b + int(i)
        
            c =round( b / len(a),1+1)
        print(c)

    elif tale == 'lcd':
        list = [int(i) for i in a]
        def lcm(i):
            result = list[0]
            for i in range(0+1, len(list)):
                result = result * list[i] // math.gcd(result, list[i])
            return result
        print(lcm(list))

    elif tale == 'gcd':
        list = [int(i) for i in a]
        print(reduce(math.gcd, list))

    elif tale == 'min':
        list = [int(i) for i in a]
        x = min(list)
        print(x)
    elif tale == 'max':
        list = [int(i) for i in a]
        y = max(list)
        print(y)