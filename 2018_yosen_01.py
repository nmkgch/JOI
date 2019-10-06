abc=list(map(int, input().split()))
a=abc[0]
b=abc[1]
c=abc[2]
coin=a
date=1
day=1
while coin<c:
    coin=coin+a
    date=date+1
    day=day+1
    if date==7:
        coin=coin+b
        date=0
print(day)