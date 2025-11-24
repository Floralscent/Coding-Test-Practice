import sys, heapq
input = sys.stdin.readline

n = int(input().rstrip())
arr = []

for _ in range(n):
    a,b = map(int, input().rstrip().split())
    arr.append((a,b))

arr.sort()
min_heapq = []
line = 1

heapq.heappush(min_heapq, arr[0][1])

for x in arr[1:]:
    while min_heapq and min_heapq[0] <= x[0] :
        heapq.heappop(min_heapq)
    heapq.heappush(min_heapq, x[1])
    line = max(line, len(min_heapq))
print(line)    
