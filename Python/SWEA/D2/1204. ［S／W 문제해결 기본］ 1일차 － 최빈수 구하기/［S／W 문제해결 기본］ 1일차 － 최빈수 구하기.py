count = [0] * 101

t = int(input()) # num_test_case

for k in range(1, t+1):
	n = int(input())
	li = list(map(int, input().split()))
	arr = [0] * 101
	for i in range(len(li)):
	    arr[li[i]] +=1
        
	max_val = 0 ; max_idx= 0
	for j in range(101):
	    if arr[j] >= max_val :
	        max_val = arr[j]
	        max_idx = j
	print("#"+str(n), max_idx)