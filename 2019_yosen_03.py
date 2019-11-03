B=[]
s = [input() for i in range(2)]
NM=list(map(int, s[0].split()))
n=NM[0]
m=(NM[1])+1
A=list(map(int, s[1].split()))
for a in range(1,m):
    b=A.count(a)
    B.append(b)
print(max(B))