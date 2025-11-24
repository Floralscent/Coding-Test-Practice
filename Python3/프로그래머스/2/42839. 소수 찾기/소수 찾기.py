from itertools import permutations
def solution(numbers):
    li = [x for x in numbers]
    ans = set()
    n = len(li)
    
    def chk(z):
        if z in ans:
            return False
        if z<=1:
            return False
        for j in range(2,int(z**(0.5))+1):
            if z%j ==0:
                return False
        return True
    
    for i in range(1,n+1):#n이 2개일때 루프를 2개까지 돌아야해서
        for permu in permutations(li,i):
            num = int("".join(permu))
            
            if chk(num):
                ans.add(num)
    
    return len(ans)