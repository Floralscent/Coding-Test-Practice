c,r = map(int, input().split())
n = int(input())

col_list = [0,c] ; row_list = [0,r]

for _ in range(n):
    a,b = map(int, input().split())
    
    if a == 0:
        row_list.append(b)
    elif a ==1:
        col_list.append(b)
#정렬
row_list.sort()
col_list.sort()

# 최대 넓이는 최대 로우의 길이와 최대 컬럼 길이의곱 
max_c = col_list[1] - col_list[0]
max_r = row_list[1] - row_list[0]

for i in range(1, len(col_list)):
    if col_list[i] - col_list[i-1] > max_c:
        max_c = col_list[i] - col_list[i-1]

for j in range(1, len(row_list)):
    if row_list[j] - row_list[j-1] > max_r:
        max_r = row_list[j] - row_list[j-1]

print(max_c*max_r)