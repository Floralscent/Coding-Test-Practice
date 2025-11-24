t = int(input()) #num of test case

for r in range(1,t+1):
	n, m = map(int, input().split())
	graph = [list(map(int, input().split())) for _ in range(n)]
	li_sum = [0] * ((n-m+1)**2)
	for i in range(len(li_sum)):
		x , y = i//(n-m+1) , i %(n-m+1)
		for j in range(x ,x+m):
			for k in range(y,y+m):
				li_sum[i] += graph[j][k]	
	print("#"+str(r), max(li_sum))