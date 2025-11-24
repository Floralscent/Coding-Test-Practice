T = int(input())

def check_row(arr):
    for i in range(9):
        if len(set(arr[i])) != 9:
            return False
    return True

def check_col(arr):
    for j in range(9):
        col = [arr[i][j] for i in range(9)]
        if len(set(col)) != 9:
            return False
    return True

def check_tbyt(arr):
    # (0,0) (0,3), (0,6) ~
    for k in range(0,9,3): #i
        for r in range(0,9,3): #j
            li = [arr[i][j] for j in range(r,r+3) for i in range(k,k+3)]
            if len(set(li)) !=9:
                   return False
    return True
            
        
for test_case in range(1, T + 1):
    #
    arr = []
    for _ in range(9):
        arr.append(list(map(int, (input().split()))))
   
    col=check_col(arr)
    row=check_row(arr)
    tbyt=check_tbyt(arr)
    check = 1 if all([col,row,tbyt]) else 0 
    print(f"#{test_case} {check}")