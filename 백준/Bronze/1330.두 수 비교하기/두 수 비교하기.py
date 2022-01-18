def limit(num):
    if num>100000 or num<-100000:
        return False
    else:
        return True

a,b = map(int,input().split())
if a== False:
    a =int(input())
elif b == False:
    b = int(input())

if a>b :
    print('>')
elif a <b :
    print('<')
else :
    print("==")