from itertools import product

def solution(users, emoticons):
    n = len(users); num = len(emoticons)
    mx = 0 ; mx_sell = 0
    per = [10,20,30,40]
    
    for p in product(per,repeat = num):
        buy = [0]*n
        dis = list(p)
        tmp =[]
        cnt = 0
        for k in range(num):
            tmp.append((int(emoticons[k]*(100-dis[k])/100)))
        #
        for j in range(n):
            for i in range(num):
                if users[j][0]<= dis[i]:
                    buy[j] += tmp[i]
            #
            if users[j][1] <= buy[j]:
                cnt +=1
                buy[j] =0
            #
        #
        if mx <cnt:
            mx =cnt
            mx_sell = sum(buy)
        elif mx == cnt:
            mx_sell = max(mx_sell, sum(buy))
    answer = [mx,mx_sell]
    return answer