s2=[]
NABS=[input() for i in range(2)]
NAB=list(map(int, NABS[0].split()))
N=NAB[0]
A=(NAB[1])-1
B=(NAB[2])
S=list(NABS[1])
for a in (S[A:B]):
    s2.insert(0,a)
del S[A:B]
s2=map(str,s2)
s2=''.join(s2)
S.insert(A,s2)
S=map(str,S)
S=''.join(S)
print(S)