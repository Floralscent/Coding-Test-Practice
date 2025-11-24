import sys
l, c = map(int, input().split())
li = list(map(str, input().split()))
li.sort()

def dfs(n,lst):
    global ans
    if n == c: #
        if len(lst) == l:
            if any(x for x in lst if x in 'aeiou'):
                cnt = lst.count("a")+lst.count("e")+lst.count("i")+lst.count("o")+lst.count("u")
                if len(lst) - cnt >=2:
                    ans.append(lst)
        return
    dfs(n+1,lst+[li[n]])
    dfs(n+1,lst)
    
ans = []

dfs(0,[])

for i in ans:
    print("".join(map(str,(i))))