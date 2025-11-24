import sys
input = sys.stdin.readline

st1 = list(input().rstrip())  # 초기 문자열
st2 = []  # 커서 오른쪽에 있는 문자들을 저장할 스택

for _ in range(int(input())):  # 명령어 개수 입력
    command = input().split()  # 명령어 입력
    
    if command[0] == 'L':  # 커서를 왼쪽으로 이동
        if st1:
            st2.append(st1.pop())
            
    elif command[0] == 'D':  # 커서를 오른쪽으로 이동
        if st2:
            st1.append(st2.pop())

    elif command[0] == 'B':  # 커서 왼쪽에 있는 문자 삭제
        if st1:
            st1.pop()
            
    else:  # 커서 왼쪽에 새로운 문자 추가
        st1.append(command[1])
        
# 스택 st2를 역순으로 st1에 합치기
st1.extend(reversed(st2))

# 결과 출력
print(''.join(st1))
