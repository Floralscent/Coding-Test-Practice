n,m = map(int,(input().split()))
li = []
cnt = 0 ; idx = n
for _ in range(n):
    li.append(int(input()))

for i in range(len(li)):
    if li[i] > m:
        idx = i
        break

for j in range(idx-1,-1,-1):
    cnt += m//li[j]
    m = m%li[j]
    if m == 0:
        break
print(cnt)