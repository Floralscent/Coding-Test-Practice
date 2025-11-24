n = input()
w = str(n)
li = []
for i in range(len(w)):
    li.append(int(w[i]))
    
li.sort(reverse = True)

for i in range(len(li)):
    print(li[i], end ='')
              