T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def rotate(ar):
    N = len(ar)
    graph = [[ar[i][j] for i in range(N-1,-1,-1)] for j in range(N)]

    return graph
    
for test_case in range(1, T + 1):
    n = int(input())
    arr = []
    for _ in range(n):
        li = list(map(int, (input().split())))
        arr.append(li)
    #
    arr_90 = rotate(arr)
    arr_180 = rotate(arr_90)
    arr_270 = rotate(arr_180)

    print(f"#{test_case}")
    for i in range(n):
        row_90 = ''.join(map(str, arr_90[i]))
        row_180 = ''.join(map(str, arr_180[i]))
        row_270 = ''.join(map(str, arr_270[i]))
        print(f"{row_90} {row_180} {row_270}")
       