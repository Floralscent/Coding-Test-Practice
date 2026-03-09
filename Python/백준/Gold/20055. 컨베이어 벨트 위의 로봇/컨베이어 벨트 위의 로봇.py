from collections import deque
import sys

n,k = map(int, (sys.stdin.readline().split()))

li = list(map(int,(input().split())))

belt = deque(li)
robot = deque([0]*n)
cnt = 1

while True:
    #
    belt.rotate(1)
    robot.rotate(1)

    #
    if robot[n-1] == 1:
        robot[n-1] = 0


    for i in range(n-1,-1,-1):
        if belt[i+1] >= 1:
                if robot[i] == 1 and robot[i+1] ==0 and belt[i+1]>0:
                    robot[i] = 0
                    robot[i+1] = 1
                    belt[i+1] -=1
                    if belt[i+1] <1:
                        k -=1
    #
    if robot[n-1] == 1:
        robot[n-1] = 0

    if belt[0] >0:
        belt[0] -= 1
        robot[0] =1
        if belt[0] <1:
            k -=1
    #
    if k<1:
        print(f"{cnt}")
        sys.exit(0)
    else:
        cnt+=1
