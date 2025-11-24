import math

def solution(fees, records):
    # info: {차량번호: 총 누적 주차시간}
    # udict: {차량번호: 현재 입차시간}
    info = {}
    udict = {}
    
    # 1. 입/출차 기록 처리
    for i in records:
        li = list(i.split())
        time = li[0]
        h = int(time[:2])
        m = int(time[3:])
        #
        uid = li[1]
        command = li[2]
        
        time_in_minutes = h * 60 + m
        
        if command == "IN":
            #
            udict[uid] = time_in_minutes
            # info 딕셔너리에 차량 번호가 없으면 0으로 초기화
            if uid not in info:
                info[uid] = 0
        
        elif command == "OUT":
            # 입차 시간 조회
            in_time = udict[uid]
            # 누적 시간에 주차 시간 추가
            info[uid] += (time_in_minutes - in_time)
            # 
            del udict[uid]

    # 2. 출차 기록이 없는 차량 처리 (23:59 출차)
    # udict에 남아있는 차량들이 출차 기록이 없는 차량임
    exit_time = 23 * 60 + 59
    for uid, in_time in udict.items():
        info[uid] += (exit_time - in_time)

    # 3. 차량 번호 순으로 정렬하여 요금 계산
    ans = []
    # 
    for uid, t in sorted(info.items()):
        # 기본 시간 이하라면 기본 요금
        if t <= fees[0]:
            tmp = fees[1]
        # 기본 시간 초과 시
        else:
            # 
            extra_time = t - fees[0]
            extra_fee = math.ceil(extra_time / fees[2]) * fees[3]
            tmp = fees[1] + extra_fee
        
        ans.append(tmp)
        
    return ans