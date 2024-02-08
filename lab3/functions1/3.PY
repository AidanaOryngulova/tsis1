def solve(numheads, numlegs):
 allchickenlegs=numheads*2
 extralegs=numlegs-allchickenlegs
 rabbitlegs=extralegs/2
 chickenlegs=numheads-rabbitlegs
 print(rabbitlegs, chickenlegs)
 
numheads=int(input())
numlegs=int(input())
solve(numheads, numlegs)


