from collections import Counter
def solution(want, number, discount):
    n_dict = {}; ans = 0
    for i in range(len(want)):
        n_dict[want[i]] = number[i]
    #
    for j in range(len(discount)-10+1):
        tmp = discount[j:j+10]
        cnt =Counter(tmp)
        if n_dict == cnt:
            ans +=1
    return ans