x = int(input('in_1: '))
fil = 1
Tr = 0
Fa = 0
for files in range(x):
    fil+=1
    memory = (input(f'in_{fil}: '))
    if str(memory).split()[-1] == 'True':
        Tr+=1
    else:
        Fa +=1
print('out:',Tr, Fa)

