n , b= map(int,input('').split(' '))
list=[]
list2=[]
list2.append(b)

while n !=-1 and b != -1:
        
        def find_factors(num):
            factors = []
            for i in range(1, num + 1):
                    if num % i == 0:
                            factors.append(i)
                    return factors
            a=find_factors(n)
            y = sum(a)
            def numberToBase(n, b):
                        if n == 0:
                            return [0]
            digits = []
            while n:
                digits.append(int(n % b))
                n //= b
                return digits[::-1]
            def list_to_number(lst):
                        return int(''.join(map(str, lst)))
            z=list_to_number(numberToBase(y,b))
            list.append(z)
        t = sum(list)
                    
        n , b= map(int,input('').split(' '))
                    
        list2.append(b)
list2.remove(-1)
# print(t)

set = set(list2)

for i in set:
    if i not in range(2,10):
            print('invalid base!')
            break
    else:
      print(t)
      break

   
       

                
                         


