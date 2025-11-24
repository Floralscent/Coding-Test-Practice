'''
def cnt_li(arr, k):
    ans = 0
    for lst in arr:
        if not any(lst):  # lst에 1이 하나도 없다면 패스
            continue
        cnt = 0
        for i in range(1, len(lst) - 1):  # 경계를 제외하고
            if lst[i] == 1:
                if cnt == 0:
                    cnt = 1  # 연속 1이 시작됨
                else:
                    cnt += 1  # 연속된 1의 길이 증가
            else:
                if cnt == k:
                    ans += 1  # 연속된 1이 k길이만큼 나왔으면 카운트
                cnt = 0  # 1이 끝났으니 cnt 초기화
        if cnt == k:  # 행 끝난 후에도 연속된 1이 k라면 카운트
            ans += 1
    return ans

T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = [[0] * (n + 2)]  # 경계 0 추가
    for _ in range(n):
        arr.append([0] + list(map(int, input().split())) + [0])  # 각 행에 경계 0 추가
    arr.append([0] * (n + 2))  # 경계 0 추가

    # 배열을 트랜스포즈
    arr_t = list(map(list, zip(*arr)))

    # 가로, 세로 방향으로 연속된 1의 길이가 k인 구간을 카운트
    ans_tc = cnt_li(arr, k) + cnt_li(arr_t, k)

    # 결과 출력
    print(f"#{test_case} {ans_tc}")
'''

def cnt_li(arr, k):
    ans = 0
    for lst in arr:
        if not any(lst):  # lst에 1이 하나도 없다면 패스
            continue
        cnt = 0
        for i in range(len(lst)):  # 경계를 제외하고
            if lst[i] == 1:
                if cnt == 0:
                    cnt = 1  # 연속 1이 시작됨
                else:
                    cnt += 1  # 연속된 1의 길이 증가
            else:
                if cnt == k:
                    ans += 1  # 연속된 1이 k길이만큼 나왔으면 카운트
                cnt = 0  # 1이 끝났으니 cnt 초기화
        if cnt == k:  # 행 끝난 후에도 연속된 1이 k라면 카운트
            ans += 1
    return ans

T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))  # 각 행에 경계 0 추가
    

    # 배열을 트랜스포즈
    arr_t = list(map(list, zip(*arr)))

    # 가로, 세로 방향으로 연속된 1의 길이가 k인 구간을 카운트
    ans_tc = cnt_li(arr, k) + cnt_li(arr_t, k)

    # 결과 출력
    print(f"#{test_case} {ans_tc}")
