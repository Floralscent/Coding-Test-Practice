T = int(input())
for test_case in range(1, T + 1):
    n= int(input())
    if n ==1:
        ans = input()
        print(f"#{test_case} {ans}")
        continue
    graph = []
    for _ in range(n):
        num = input()
        graph.append([int(x) for x in num])
    #print(graph)
    ans = 0; c = n//2; k =0
    for i in range(n):
        if  i == 0:
            ans+=graph[i][c]
            k+=1
        elif 0<i<c:
            ans += sum(graph[i][c-k:c+k+1])
            k+=1
        elif c<=i<n:
            ans += sum(graph[i][c-k:c+k+1])
            k-=1
    print(f"#{test_case} {ans}")