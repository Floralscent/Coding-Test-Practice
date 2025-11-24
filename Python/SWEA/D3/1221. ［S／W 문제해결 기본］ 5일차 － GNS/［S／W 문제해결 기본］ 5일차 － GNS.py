T = int(input())
dic_a2n = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
dic_n2a = {0:"ZRO", 1:"ONE", 2:"TWO", 3:"THR", 4:"FOR", 5:"FIV", 6:"SIX", 7:"SVN", 8:"EGT", 9:"NIN"}

for test_case in range(1, T + 1):
    wd , l = map(str, input().split())
    li = list(input().split())
    num_li = [] ; dic_li = []
    for i in range(len(li)):
        num_li.append(dic_a2n[li[i]])
    #
    num_li.sort()
    for j in range(len(num_li)):
        dic_li.append(dic_n2a[num_li[j]])
    ans = ""
    for k in range(len(num_li)):
        ans+= str(dic_li[k]) + " "
        
    print(f"{wd} {ans}")