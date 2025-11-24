'''
import sys
t = int(input())
mx = int(1e4)
if t == 1:
    print("1/1")
    sys.exit(0)
cnt = 2 ; i = 0; j= 1

while t != cnt:

    chk = i+j
    if chk%2 == 0:# 오른위
        nx = i-1; ny = j+1
        if 0<=nx<mx and 0<=ny<mx:
            pass
        else:
            nx = 0; ny = j+1
        #
    else: #왼아래
        nx = i+1; ny=j-1
        if 0<=nx<mx and 0<=ny<mx:
            pass
        else:
            nx = i+1; ny = 0
    i = nx;j=ny
    cnt+=1

print(f"{i+1}/{j+1}")
'''

X = int(input())

line = 1
while X > line:
    X -= line
    line += 1

if line % 2 == 0:  # 짝수 대각선일 경우 (위-오른쪽)
    a = X             
    b = line - X + 1 
else:  # 홀수 대각선일 경우 (아래-왼쪽)
    a = line - X + 1 
    b = X            
print(f"{a}/{b}")