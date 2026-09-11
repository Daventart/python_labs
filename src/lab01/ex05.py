name = input()
upper = ''.join([a for a in name if a.isupper()])
print(f'Инициалы: {upper}')
print(f'Длина: {len(' '.join(name.split()))}')