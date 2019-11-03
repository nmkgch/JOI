NA=[input() for i in range(2)]
N=int(NA[0])
A=list(map(int, NA[1].split()))
umi=0
sima=0
saidai=0
hantei=False
while umi<max(A):
    for a in A:
        if umi<a and hantei:
            continue
        elif umi<a:
            hantei=True
            sima+=1
        else:
            hantei=False
    if saidai<sima:
        saidai=sima
    sima=0
    umi+=1
    hantei=False
print(saidai)