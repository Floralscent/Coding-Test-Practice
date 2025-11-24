def solution(s):
    s = s.rstrip("}").lstrip("{").split("},{")
    li = []
    s.sort(key = lambda x: len(x))
    for i in s:
        num = list(map(int,(i.split(","))))
        #print(num)
        for x in num:
            if not x in li:
                li.append(x)
    return li if 1<=len(li) <=500 else 0