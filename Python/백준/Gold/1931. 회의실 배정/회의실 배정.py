# Python 풀이
N = int(input())
arr = []

for _ in range(N):
    a,b = map(int,input().split())
    arr.append((a,b))

arr.sort(key=lambda x : (x[1],x[0])) 
#arr 구조는 [(a1,b1),(a2,b2)....]인 상태인데 b의 크기를 기준으로 정렬

room = 1 # 처음에는 무조건 회의 하나는 열린다
check = arr[0][1] # 가장 빨리 끝나는 회의가 첫 기준점
for idx in range(1,N):
    if arr[idx][0] >= check: # 직전 회의 끝나는 시간이 다음 회의 시작시간과 같거나 그 이후 일때
        check = arr[idx][1] # 다음 회의 끝 시간을 갱신하고 
        room += 1 # 방을 하나 늘림

print(room)
