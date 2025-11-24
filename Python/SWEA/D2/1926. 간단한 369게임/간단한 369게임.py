n = int(input())

for i in range(1,n+1):
    w = str(i); cnt = 0
    if "3" or "6" or "9" in w:
        cnt += w.count("3")
        cnt += w.count("6")
        cnt += w.count("9")
    if cnt > 0 :
        print("-"*cnt,end = " ")
    else:
        print(i, end = " ")