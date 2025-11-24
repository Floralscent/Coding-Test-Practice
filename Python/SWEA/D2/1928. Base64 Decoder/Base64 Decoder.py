'''
TGlmZSBpdHNlbGYgaXMgYSBxdW90YXRpb24u
U3VzcGljaW9uIGZvbGxvd3MgY2xvc2Ugb24gbWlzdHJ1c3Qu
VG8gZG91YnQgaXMgc2FmZXIgdGhhbiB0byBiZSBzZWN1cmUu
T25seSB0aGUganVzdCBtYW4gZW5qb3lzIHBlYWNlIG9mIG1pbmQu
QSBmdWxsIGJlbGx5IGlzIHRoZSBtb3RoZXIgb2YgYWxsIGV2aWwu
>>
#1 Life itself is a quotation.
#2 Suspicion follows close on mistrust.
#3 To doubt is safer than to be secure.
#4 Only the just man enjoys peace of mind.
#5 A full belly is the mother of all evil.
'''

t = int(input())
base64_table = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")
for i in range(1,t+1):
    line = ""
    word = input()
    li= [word[q:q+4] for q in range(0,len(word),4)]
    for j in range(len(li)):
        wd = ""
        for k in range(4):
            tmp = base64_table.index(li[j][k])
            wd+=format(tmp, "06b")
        #wd를 이제 8개씩 쪼개
        li_8 = [wd[r:r+8] for r in range(0, len(wd), 8)]
        for l in range(len(li_8)):
            num = int(li_8[l],2)
            line += chr(num)
        #이걸 반복하면 한 문장
    print("#"+str(i), line)
        