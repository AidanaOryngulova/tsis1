import math
def my_func():
 x = list(map(int,input().split()))
 res =[]
 for n in x:
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i==0:
            break
    else:
        res.append(n)
 print(res)
my_func()