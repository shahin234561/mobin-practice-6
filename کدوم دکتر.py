a = int(input(''))
b = int(input(''))




x = bin(a ^ b)
m=0
for i in x:
    if i=='1':
        m=m+1

print(m)
