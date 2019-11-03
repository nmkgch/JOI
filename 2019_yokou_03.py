kazu=int(input())
namae=[input() for i in range(kazu)]
namae2=' '.join(map(str,namae))
namae3=namae2.lower()
namae4=namae3.split()
namae5='\n'.join(namae4)
print(namae5)