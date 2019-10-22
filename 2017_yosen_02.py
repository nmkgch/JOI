j=None
m2=[]
# s=[input() for i in range(2)]
# N=int(s[0])
# A=list(map(int, s[1].split()))

N=7
A=[0,0,1,0,1,1,0]

for t in range(N):
    masu=A[0]
    if masu==1 and j:
        men+=1
    elif masu==1:
        men=1
        j=True
    elif j:
        m2.append(men)        
        j=False
    del A[0]
men=(max(m2))+1
print(men)