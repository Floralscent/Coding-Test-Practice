def solution(numbers, target):
    ans = 0
    n = len(numbers)
    def dfs(k,tmp):
        nonlocal ans
        
        if n == k:
            if tmp == target:
                ans+=1
            return 
        #
        dfs(k+1,tmp+numbers[k])
        dfs(k+1,tmp-numbers[k])
    
    dfs(0,0)
    answer = ans
    return answer