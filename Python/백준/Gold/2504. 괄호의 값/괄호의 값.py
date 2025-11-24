import sys
'''
word = list(input())

s = []
ans = 0
for i in range(len(word)):
    if word[i] == "(" or word[i] == "[":
        s.append(word[i])
    else: # 여는 괄호가 아닌경우
        if type(s[-1]) == int: ## 숫자가 나왔음 그럼 다음에 숫자가 아닌거 나올때까지 파악하고
            # 숫자 - 숫자면 더하기, 숫자 - 맞는 괄호면 곱하기, 숫자 - 안맞는 괄호면 때려치기
            idx = -1
            while type(s[idx]) == int:
                idx -= 1
            # idx를 늘려서 숫자 아닌거 찾으면 그게 idx에 반영
            idx +=1
            tmp = 0
            for i in range(idx*-1):
                tmp += int(s.pop())
            ### 숫자 연속으로 나오는거 해결 , 숫자 뒤에 이제 짝이 맞으면 곱하기
            tmp_word = s.pop()
            if word[i] == ")" and tmp_word == "(":
                s.append(tmp*2)
                print("mul 2")
            elif word[i] == "]" and tmp_word == "[":
                s.append(tmp*3)
                print("mul 3")
            else: # 숫자도 아니고 괄호의 짝도 안맞는경우
                print(0)
                exit(0)
        else:
            tmp_word = s.pop()
            if word[i] == ")" and tmp_word == "(":
                s.append(2)
                print("Plus 2")
            elif word[i] == "]" and tmp_word == "[":
                s.append(3)
                print("Plus 3")
            else: # 숫자도 아니고 괄호의 짝도 안맞는경우
                print(0)
                exit()

print(s)


'''


word = list(input())
s = []

for ch in word:
    if ch == '(' or ch == '[':
        s.append(ch)
    else:
        if not s:  # 스택 비었는데 닫는 괄호 → 오류
            print(0)
            exit(0)

        if isinstance(s[-1], int):  # 숫자 누적된 상태라면
            tmp = 0 # 숫자 나왔어 근데 뺀다음에 숫자면 누적해서 덧셈
            while s and isinstance(s[-1], int):
                tmp += s.pop()
            
            if not s:  # 숫자 다 빼고 나서도 괄호 없으면 오류
                print(0)
                exit(0)

            top = s.pop()
            if ch == ')' and top == '(':
                s.append(tmp * 2)
                #print("mul 2")
            elif ch == ']' and top == '[':
                s.append(tmp * 3)
                #print("mul 3")
            else:
                print(0)
                exit(0)

        else:  # 바로 괄호 닫히는 경우: () 또는 []
            top = s.pop()
            if ch == ')' and top == '(':
                s.append(2)
                #print("Plus 2")
            elif ch == ']' and top == '[':
                s.append(3)
                #print("Plus 3")
            else:
                print(0)
                exit(0)

# 최종 결과: 괄호가 남아있으면 잘못된 구조
for i in s:
    if not isinstance(i, int):
        print(0)
        exit(0)

print(sum(s))
