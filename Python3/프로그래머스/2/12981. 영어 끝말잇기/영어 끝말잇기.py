def solution(n, words):
    # cnt = 0
    li = []
    for i in range(len(words)):
        if i == 0:
            li.append(words[i])
            continue
            # cnt +=1
            
        if li[-1][-1] == words[i][0]:
            if not words[i] in li:
                li.append(words[i])
                # cnt+=1
            else: 
                cnt = len(li)+1
                people_num = cnt % n
                if people_num  == 0:
                    people_num = n
            # loof_num
                if cnt <= n:
                    loof_num = 1
                else:
                    loof_num = len(li) //n +1
                return [people_num, loof_num]
        else:
            # people_num
            cnt = len(li)+1
            people_num = cnt % n
            if people_num  == 0:
                people_num = n
            # loof_num
            if cnt <= n:
                loof_num = 1
            else:
                loof_num = len(li) //n +1
            return [people_num, loof_num]
    
    # print(*li)
    return [0,0]
