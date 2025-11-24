T = 10

def cnt(arr):
    global ans
    for lst in arr:
        for i in range(1, 101): 
            for j in range(len(lst)-i+1):
                li = lst[j:j+i]
                if li == li[::-1]:
                    ans = max(ans, i)

for _ in range(1, T + 1):
    t = int(input())
    arr = [list(input().strip()) for _ in range(100)]
    
    ans = 0  
    arr_t = list(map(list, zip(*arr)))
    cnt(arr)
    cnt(arr_t)

    print(f"#{t} {ans}")
