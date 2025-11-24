word = list(input())
boom = list(input())
check_idx = len(boom)
ans = []
for i in range(len(word)):
    ans.append(word[i])
    # 앞자리로 안하는 이유는 연쇄 고려
    if ans[-1] == boom[-1]:
        if len(ans)>= check_idx and ans[-check_idx:] == boom:
            del ans[-check_idx:]
            
if len(ans) == 0:
    print("FRULA")

else:
    print(''.join(map(str,ans)))
        
        

