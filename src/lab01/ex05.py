name = input("ФИО: ")
upper = ''.join([a for a in name if a.isupper()])
print(f'Инициалы: {upper}.')
print(f'Длина (символов): {len(' '.join(name.split()))}')