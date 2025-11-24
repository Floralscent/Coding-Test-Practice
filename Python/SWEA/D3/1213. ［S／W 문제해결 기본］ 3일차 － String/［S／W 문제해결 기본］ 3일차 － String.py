T = 10
for _ in range(1, T + 1):
    #
    t = int(input())
    wd = input()
    word = input()
    cnt = 0
    if wd in word:
        cnt = word.count(wd)
        
    print(f"#{t} {cnt}")