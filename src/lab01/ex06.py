x = int(input())
files = 0
Tr = 0
Fa = 0
for files in range(x):
    files+=1
    memory = (input(f'in_{files}: '))
    if str(memory).split()[-1] == 'True':
        Tr+=1
    else:
        Fa +=1
print(Tr, Fa)

