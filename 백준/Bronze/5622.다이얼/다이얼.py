alpahbet = input().lower()
dial = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
time = 0

for i in range(len(alpahbet)):
    for j in dial:
        if alpahbet[i] in j :
            time += dial.index(j) + 3
print(time)