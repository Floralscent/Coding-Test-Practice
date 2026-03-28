import sys

input = sys.stdin.readline

n, l = map(int, (input().split()))

li = list(map(int, (input().split())))

num_cnt = [0]*100001
ans = 0
s_i = 0
end_i = 0

for end_i in range(len(li)):
    num_cnt[li[end_i]] +=1
    
    while num_cnt[li[end_i]] >l:
        num_cnt[li[s_i]] -=1
        s_i +=1
    #
    ans = max(ans, end_i-s_i+1 )
#
print(ans)