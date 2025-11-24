def solution(s):
    d = len(s)
    s = s*2
    cnt = 0
    
    for j in range(d):
        li = []
        valid = True
        for i in s[j:j+d]:  # s[j:] 대신 원래 배열의 길이만큼만 순회
            if i == "(":
                li.append(i)
            elif i == ")":
                if li and li[-1] == '(':
                    li.pop()
                else:
                    valid = False
                    break
            
            if i == "[":
                li.append(i)
            elif i == "]":
                if li and li[-1] == '[':
                    li.pop()
                else:
                    valid = False
                    break

            if i == "{":
                li.append(i)
            elif i == "}":
                if li and li[-1] == '{':
                    li.pop()
                else:
                    valid = False
                    break
        
        if valid and not li:  # 괄호가 모두 짝이 맞고 스택이 비었으면 카운트 증가
            cnt += 1
                
    return cnt
