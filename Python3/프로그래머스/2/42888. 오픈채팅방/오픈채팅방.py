def solution(record):
    
    uid_info = {}
    for rd in record:
        parts = rd.split()
        command = parts[0]
        
        # 
        if command == "Enter" or command == "Change":
            uid = parts[1]        
            nickname = parts[2]
            uid_info[uid] = nickname

    #
    answer = []
    for rd in record:
        parts = rd.split()
        command = parts[0]
        uid = parts[1]
        
        
        if command == "Enter":
            answer.append(f"{uid_info[uid]}님이 들어왔습니다.")
        elif command == "Leave":
            answer.append(f"{uid_info[uid]}님이 나갔습니다.")
        
            
    return answer