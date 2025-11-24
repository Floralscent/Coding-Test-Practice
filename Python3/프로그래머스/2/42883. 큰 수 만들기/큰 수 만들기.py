def solution(number, k):
    
    stack = []
    for digit in number:
        while stack and k > 0 and stack[-1] < digit:
            stack.pop()
            k -= 1
        #
        stack.append(digit)
        
    if k > 0:
        stack = stack[:-k] #만약에 k가 남으면 숫자 높은애들이 아래니까 뒤에 날리기
    
    return "".join(stack)