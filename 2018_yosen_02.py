cnt4=0
s = [input() for i in range(4)]
kazu=int(s[0])
basyo=list(map(int, s[1].split()))
sousa=int(s[2])
bango=list(map(int, s[3].split()))
for cnt in range(sousa):
    cnt2=(bango[cnt])
    cnt3=(basyo[cnt2-1])+1
    if not cnt2==kazu:
        cnt4=(basyo[cnt2])
        del basyo[cnt2]
    del basyo[cnt2-1]
    if cnt3>=2019:
        cnt3=2019
    if cnt3==cnt4:
        cnt3=cnt3-1
    basyo.append(cnt3)
    if not cnt2==kazu:
        basyo.append(cnt4)
    basyo.sort()
moji=map(str,basyo)
k='\n'.join(moji)
print(k)