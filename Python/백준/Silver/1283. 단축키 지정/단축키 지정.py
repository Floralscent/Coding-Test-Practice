import sys

n = int(sys.stdin.readline())
used_keys = set()

for _ in range(n):
    words = sys.stdin.readline().split()
    found_bool = False

    ## 1.
    for i in range(len(words)):
        first_char = words[i][0]
        if first_char.upper() not in used_keys:
            used_keys.add(first_char.upper())
            words[i] = "[" + first_char + "]" + words[i][1:]
            found_bool = True
            break
    
    ## 2.
    if not found_bool:
        for i in range(len(words)):
            for j in range(len(words[i])):
                char = words[i][j]
                if char.upper() not in used_keys:
                    used_keys.add(char.upper())
                    words[i] = words[i][:j] + "[" + char + "]" + words[i][j+1:] #
                    found_bool = True
                    break
            if found_bool: break
            
    print(" ".join(words))