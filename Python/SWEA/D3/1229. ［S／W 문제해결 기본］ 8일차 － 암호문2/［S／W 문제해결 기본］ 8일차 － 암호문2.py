T = 10
for test_case in range(1, T + 1):
    #
    l = int(input())
    li = list(map(int, (input().split())))
    cm_l = int(input())
    cm = list(input().split())
    i = 0
    while i <len(cm):
        if cm[i] == "I":
            w = int(cm[i+1]) ; n = int(cm[i+2])
            num = cm[i+3:i+3+n]
            li = li[:w]+num+li[w:]
            i+=(3+n)
        elif cm[i] == "D":
            w = int(cm[i+1])
            n = int(cm[i+2])
            li = li[:w]+li[w+n:]
            i+=3
    #
    ans = " ".join(str(li[j]) for j in range(10))
    
    print(f"#{test_case} {ans}")