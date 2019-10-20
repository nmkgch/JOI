OX=0
s = [input() for i in range(2)]
kazu=s[0]
stamp=list(s[1])

# kazu=5
# stamp=['O','X','X','O','X']

while stamp!=['O'] and stamp!=['X'] and stamp!=[]:
    sta1=stamp[0]
    del stamp[0]
    sta2=stamp[0]
    if sta1=='O' and sta2=='X':
        del stamp[0]
        OX+=1
    if sta1=='X' and sta2=='O':
        del stamp[0]
        OX+=1
print(OX)