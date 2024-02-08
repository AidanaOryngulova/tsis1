
from itertools import permutations 
def permstr():
 ren=str(input())
 perm=permutations(ren)
 for i in perm:
  print(''.join(i))

permstr()