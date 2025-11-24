# x' = y+1; y' = r-x

import sys

def position(word):
    if word == "R": #o
        nx = 0 ; ny = 1 
    elif word == "L": #o
        nx = 0 ; ny = -1
    elif word == "B": #o
        nx = 1 ; ny = 0
    elif word == "T": #o
        nx = -1 ; ny = 0
    elif word == "RT": #o
        nx = -1 ; ny = 1
    elif word == "LT": #o
        nx = -1 ; ny = -1
    elif word == "RB": #o
        nx = 1 ; ny = 1
    elif word == "LB": #o
        nx = 1 ; ny = -1
    return nx,ny

king, rock, n = map(str, sys.stdin.readline().split())
n = int(n)
king_x = ord(king[0])-64 ; king_y = int(king[-1])
rock_X = ord(rock[0])-64 ; rock_y = int(rock[-1])

king_x , king_y = 8 - king_y, king_x -1
rock_x, rock_y = 8 - rock_y, rock_X -1

#print(rock_x,rock_y)

for _ in range(n):
    word = input()
    nx, ny = position(word)

    # 킹이 움직이는 조건은 다음과 같다
    #print(king_x,king_y) 
    if 0<= king_x+nx < 8 and 0<= king_y+ny < 8: # 다음 움직임이 체스판 이내일것
        king_x += nx; king_y += ny
        if king_x == rock_x and king_y == rock_y: # 킹의 다음 움직임이 돌과 같냐 여부
            if not(0<= rock_x+nx < 8 and 0<= rock_y+ny <8 ): # 그치만 이때 돌이 이동경로를 막을경우 움직이지 말아라
                king_x -= nx; king_y -= ny
            else:
                rock_x += nx; rock_y += ny


king_x , king_y = king_y+1, 8 - king_x
rock_x, rock_y = rock_y+1, 8- rock_x

print(chr(king_x+64)+str(king_y))
#print(rock_x)
print(chr(rock_x+64)+str(rock_y))


