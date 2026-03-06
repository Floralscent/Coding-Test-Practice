import sys

w = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()
# 재귀 시간 복잡도 가지치기를 위해 w ->t가 아닌
# t-> w 가능여부 찾기
def chk(word,target):
    if len(word) == len(target):
        if word == target:
            print(1)
            sys.exit(0)
    #
        return

    if word[-1] == "A":
        wd = word[:-1]
        chk(wd,target)
    if word[0] == "B":
        wd = word[1:][::-1]
        chk(wd,target)
chk(t,w)
    
print(0)
