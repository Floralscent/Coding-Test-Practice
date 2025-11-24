import sys
from itertools import combinations
input = sys.stdin.readline
l, k = map(int,(input().split()))
if k <5:
    print(0)
    exit(0)

N = k-5
basic_lst = ["a","n","t","i","c"]
basic_lst = set(basic_lst)
word_lst = set()

li = []
for _ in range(l):
    word = set(input().strip())
    li.append(word)
    tmp = word - basic_lst
    word_lst = word_lst | tmp

if len(word_lst) <= N:
    print(l)
    exit(0)
    
ans =0

for comb in combinations(word_lst,N):
    ba_lst = basic_lst | set(comb)
    cnt = 0
    for word in li:
        if word <= ba_lst:
            cnt +=1
    ans = max(ans,cnt)   

print(ans)