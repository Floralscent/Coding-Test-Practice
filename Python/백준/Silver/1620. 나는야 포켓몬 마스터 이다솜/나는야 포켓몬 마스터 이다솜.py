import sys
input = sys.stdin.readline

n, m = map(int, input().split())
al_to_num = {}
num_to_al = {}

for j in range(1, n + 1):
    po = input().strip()
    al_to_num[po] = j
    num_to_al[j] = po

for k in range(m):
    ip = input().strip()
    if ip.isdigit():
        print(num_to_al[int(ip)])
    else:
        print(al_to_num[ip])
