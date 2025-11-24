arr = list(map(str,input()))
tot = 0
temp =[]

for idx in range(len(arr)):
    if arr[idx] == '(':
        temp.append(arr[idx])
    elif arr[idx] == ')':
        # )가 왔을때 직전이 (면 레이저
        if arr[idx-1] == '(':
            temp.pop()
            tot += len(temp)
        else : # 막대 ( 가 생기면 조각 하나 늘음
            temp.pop()
            tot += 1
print(tot)
           