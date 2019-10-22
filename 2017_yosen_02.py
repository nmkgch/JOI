s=[input() for i in range(2)]
N=int(s[0])
A=list(map(int, s[1].split()))

renzoku = 0
saidai = 0

for i in A:
    if i == 1:
        renzoku += 1
        if saidai < renzoku:
            saidai = renzoku
    else:
        renzoku = 0

print(saidai+1)