T = int(input())

for test_case in range(1, T + 1):
    n, wd = input().split()
    n = int(n)
    ans = ""

    for i in range(n):
        w = format(int(wd[i], 16), '04b') 
        ans += w

    print(f"#{test_case} {ans}")
