def format_record(rec: tuple[str, str, float]) -> str:
        if type(rec) != tuple:
                raise TypeError('Запись обязана быть кортежем')
        if len(rec) != 3:
                raise ValueError('Недостаточно данных или перебор')
        fio, group, gpa = rec
        parts = fio.split()
        group = group.strip()

        if type(fio)!= str or type(group) != str:
                raise TypeError('ФИО и Группа - не строки')
        if type(gpa) != int and type(gpa) != float:
                raise TypeError('GPA обязан быть числовым значением')
        if gpa < 0 or gpa > 5:
               raise ValueError('GPA не в нужном диапазоне')
        if len(parts) != 2 and len(parts) != 3:
                raise ValueError('Мало данных в имени')
        if group == "":
            raise ValueError("Группа пустая")
        
        surname = parts[0].capitalize()
        inits = ''
        for i in range(1, len(parts)):
               if i > 2:
                      break
               inits += parts[i][0].upper() + '.'
        return(f'{surname} {inits},гр {group},GPA{gpa: .2f}')

# Тест кейсы
print(
    f'format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)) ->',
    format_record(("Иванов Иван Иванович", "BIVT-25", 4.6))
)

print(
    f'format_record(("Петров Пётр", "IKBO-12", 5.0)) ->',
    format_record(("Петров Пётр", "IKBO-12", 5.0))
)

print(
    f'format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)) ->',
    format_record(("Петров Пётр Петрович", "IKBO-12", 5.0))
)

print(
    f'format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)) ->',
    format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999))
)

try:
    print(
        f'format_record(("", "BIVT-25", 4.6)) ->',
        format_record(("", "BIVT-25", 4.6))
    )
except (ValueError, TypeError) as error:
    print(f'format_record(("", "BIVT-25", 4.6)) -> {type(error).__name__}: {error}')


try:
    print(
        f'format_record(("Иванов Иван", "", 4.6)) ->',
        format_record(("Иванов Иван", "", 4.6))
    )
except (ValueError, TypeError) as error:
    print(f'format_record(("Иванов Иван", "", 4.6)) -> {type(error).__name__}: {error}')


try:
    print(
        f'format_record(("Иванов Иван", "BIVT-25", "4.6")) ->',
        format_record(("Иванов Иван", "BIVT-25", "4.6"))
    )
except (ValueError, TypeError) as error:
    print(f'format_record(("Иванов Иван", "BIVT-25", "4.6")) -> {type(error).__name__}: {error}')