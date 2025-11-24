T = int(input())

def chk(arr, n, m):
    for lst in arr:
        for i in range(n - m + 1):  
            tmp = lst[i:i + m]
            if tmp == tmp[::-1]:
                return "".join(tmp)
    return None

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    arr_t = list(map(list, zip(*arr)))  

    ans = chk(arr, n, m)
    if not ans:
        ans = chk(arr_t, n, m)

    print(f"#{test_case} {ans}")
