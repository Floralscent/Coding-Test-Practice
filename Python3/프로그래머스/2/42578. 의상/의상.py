## 종류1 +1 x 종류2 +1 x 종류3 +1 x 종류4 +1 x 종류5 +1 -1

def solution(clothes):
    dict = {}
    
    for dress,c in clothes:
        if c in dict:
            dict[c] +=1
            
        else:
            dict[c] = 1
    ans = 1        
    for key in dict.keys():
        ans *= (dict[key]+1)
        
    ans = ans -1
    return ans