a2=[]
Card=[input() for i in range(2)]
N=Card[0]
a=list(map(int,Card[1].split()))
for b in a:
    a2.insert(0,b)
a2=map(str,a2)
a2=' '.join(a2)
print(a2)