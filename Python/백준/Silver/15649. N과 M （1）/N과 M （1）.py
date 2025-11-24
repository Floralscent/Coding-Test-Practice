from itertools import permutations
import sys

a,b = map(int, input().split())

li = [x for x in range(1,a+1)]

for i in permutations(li,b):
    i = list(i)
    print(*i)