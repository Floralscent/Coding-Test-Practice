import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    word,rd,ra,rb = map(str, (input().split()))

    ra = format(int(ra), '03b')  
    rd = format(int(rd), '03b')
    

    if word[-1] == "C":
        op_r = "1"
        rb = format(int(rb), '04b')
    else:
        op_r = "0"
        word += "N"
        rb = format(int(rb), '03b')

    
    if word[:-1] == "ADD":
        word = "0000"
    elif word[:-1] == "SUB":
        word = "0001"
    elif word[:-1] == "MOV":
        word = "0010"
    elif word[:-1] == "AND":
        word = "0011"
    elif word[:-1] == "OR": #
        word = "0100"
    elif word[:-1] == "MULT":
        word = "0110"
    elif word[:-1] == "LSFTL":
        word = "0111"
    elif word[:-1] == "LSFTR":
        word = "1000"
    elif word[:-1] == "ASFTR":
        word = "1001"
    elif word[:-1] == "RL":
        word = "1010"
    elif word[:-1] == "RR":
        word = "1011"
    elif word[:-1] == "NOT":
        word = "0101"

    ##
    if op_r == "0":
        code = word+op_r+"0"+rd+ra+rb+op_r
        # print(rd,ra,rb,op_r)
    else:
        code = word+op_r+"0"+rd+ra+rb
        
    print(code)
    