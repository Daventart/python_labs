# Лабораторная работа №7. Поиск, сортировка и измерение времени

**Лисёнков Алексей, БИВТ-26-6-1**


Запуск из корня репозитория:

```
python -m src.lab07.check
python -m src.lab07.bench
```


## 1. Поиск (`search.py`)

### `linear_search`

Идёт по списку слева направо и возвращает индекс первого элемента, равного `x`. Если список закончился, возвращает `-1`. Порядок элементов не важен.

```python
def linear_search(nums, x):
    """Индекс первого вхождения x или -1.
    """
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1
```

### `binary_search`

Требует отсортированный список. Сравнивает `x` с серединным элементом и отбрасывает ту половину, где `x` быть не может. Пока `lo <= hi`, область поиска не пуста; когда границы разошлись, элемента нет. На неотсортированном списке результат не определён.

```python
def binary_search(sorted_nums, x):
    """Индекс x в отсортированном по возрастанию списке или -1.
    На неотсортированном списке результат не определён.
    """
    lo = 0
    hi = len(sorted_nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_nums[mid] == x:
            return mid
        if sorted_nums[mid] < x:
            lo = mid + 1  
        else:
            hi = mid - 1  
    return -1
```

### `two_sum_brute`

Перебирает все пары индексов `(i, j)` с `i < j` и возвращает первую пару с нужной суммой, а если такой нет, то `None`.

```python
def two_sum_brute(nums, target):
    """Пара индексов (i, j), i < j, nums[i] + nums[j] == target, или None.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None
```

### `two_sum_fast`

Идёт по списку один раз и хранит в словаре `seen` уже просмотренные значения с их индексами. Для каждого числа проверяет, есть ли в словаре `target − число`. Проверка `in` у словаря не перебирает ключи, поэтому проход линейный.

```python
def two_sum_fast(nums, target):
    """То же, что two_sum_brute, но за один проход со словарём.
    """
    seen = {}
    for j in range(len(nums)):
        need = target - nums[j]
        if need in seen:
            return (seen[need], j)  
        seen[nums[j]] = j
    return None
```

## 2. Сортировки (`sorting.py`)


### `bubble_sort`

Проходит по списку и меняет местами соседей, стоящих не по порядку; после каждого прохода самый большой из оставшихся оказывается в конце. Если за проход не было ни одного обмена, цикл прерывается: список уже отсортирован.

```python
def bubble_sort(nums):
    """Новый список, отсортированный по возрастанию. Исходный не меняется.
    """
    a = list(nums)  
    n = len(a)
    for end in range(n - 1, 0, -1):
        swapped = False
        for i in range(end):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        if not swapped:  
            break
    return a
```

### `insertion_sort`

Берёт очередной элемент и сдвигает его влево по отсортированной части: большие элементы смещаются вправо, а сам элемент встаёт в освободившуюся ячейку.

```python
def insertion_sort(nums):
    """Тот же контракт, что у bubble_sort."""
    a = list(nums)
    for i in range(1, len(a)):
        item = a[i]
        j = i - 1
        while j >= 0 and a[j] > item:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = item
    return a
```

### `selection_sort`

На каждом шаге находит минимум в неотсортированной части обычным циклом (без `min`) и обменом ставит его на текущую позицию.

```python
def selection_sort(nums):
    """Тот же контракт, что у bubble_sort."""
    a = list(nums)
    n = len(a)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
    return a
```

## 3. Проверка против эталона (`check.py`)

### `check_sorting`

На 100 случайных списках (длина 0–50, значения −100…100, с повторами) сравнивает `fn(nums)` с `sorted(nums)` и проверяет, что исходный список не изменился.

```python
def check_sorting(fn, trials=100) -> int:
    """Сравнивает fn(nums) с sorted(nums) и проверяет, что исходный список цел.
    Возвращает число проведённых проверок.
    """
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {original}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список: было {original}, стало {nums}"
    return trials
```

### `check_search`

На 100 случайных списках ищет число вне диапазона, первый, последний и случайный элемент. Линейный поиск сверяется с `list.index` (`ValueError` превращается в `-1`), а бинарный проверяется на отсортированной копии: при повторах допустим любой индекс, лишь бы по нему лежал `x`.

```python
def check_search() -> int:
    """Сравнивает linear_search с list.index, а binary_search проверяет по содержимому.
    Возвращает число проведённых проверок.
    """
    checks = 0
    for _ in range(100):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        sorted_nums = sorted(nums)
        targets = [101]
        if nums:
            targets += [nums[0], nums[-1], random.choice(nums)]

        for x in targets:
            try:
                expected = nums.index(x)
            except ValueError:
                expected = -1
            got = linear_search(nums, x)
            assert got == expected, f"linear_search({nums}, {x}) = {got}, ожидали {expected}"

            got = binary_search(sorted_nums, x)
            if x in sorted_nums:
                assert 0 <= got < len(sorted_nums), f"binary_search({sorted_nums}, {x}) вернул {got}"
                assert sorted_nums[got] == x, f"binary_search({sorted_nums}, {x}) = {got}, а там не x"
            else:
                assert got == -1, f"binary_search({sorted_nums}, {x}) = {got}, ожидали -1"
            checks += 1
    return checks
```

### `check_two_sum`

Полным перебором собирает список `expected` со всеми подходящими парами. Если пары есть, оба решения обязаны вернуть одну из них (какую именно, не важно), если нет, то `None`.

```python
def check_two_sum(trials=100) -> int:
    """Оба two_sum должны вернуть одну из подходящих пар, а если пар нет, то None.
    Возвращает число проведённых проверок.
    """
    for _ in range(trials):
        n = random.randint(0, 30)
        nums = [random.randint(-50, 50) for _ in range(n)]
        target = random.randint(-100, 100)
        expected = []
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    expected.append((i, j))

        brute = two_sum_brute(nums, target)
        fast = two_sum_fast(nums, target)
        info = f"nums={nums}, target={target}, brute={brute}, fast={fast}"
        if expected:
            assert brute in expected, "two_sum_brute вернул неверную пару: " + info
            assert fast in expected, "two_sum_fast вернул неверную пару: " + info
        else:
            assert brute is None, "two_sum_brute нашёл пару, которой нет: " + info
            assert fast is None, "two_sum_fast нашёл пару, которой нет: " + info
    return trials

```

### Запуск и результат

```python
if __name__ == "__main__":
    random.seed(42)
    total = 0
    for fn in (bubble_sort, insertion_sort, selection_sort):
        total += check_sorting(fn)
    total += check_search()
    total += check_two_sum()
    print(f"OK: {total} проверок пройдено")
```

```
$ python -m src.lab07.check
OK: 791 проверок пройдено
```

![791 проверка](../../images/lab07/791proverk.png)

## 4. Бенчмарк (`bench.py`)

### `bench_sorts`

Замеряет `sorted` и три свои сортировки на n = 1 000, 10 000 и 100 000. Перед замером на n = 1 000 проверяет, что ответ верный. Возвращает список кортежей `(task, n, impl, seconds)`.

```python
def bench_sorts() -> list[tuple[str, int, str, str]]:
    """Замеряет sorted и три свои сортировки, возвращает список кортежей."""
    random.seed(42)
    rows = []
    sizes = [1_000, 10_000, 100_000]
    funcs = [
        ("bubble_sort", bubble_sort),
        ("insertion_sort", insertion_sort),
        ("selection_sort", selection_sort),
    ]
    for n in sizes:
        data = [random.randint(-1_000_000, 1_000_000) for _ in range(n)]
        time_s = timeit.timeit(lambda: sorted(data), number=10) / 10
        rows.append(("sorting", n, "sorted", f"{time_s:.6f}"))

        for name, fc in funcs:
            if n <= 10_000:
                if n == 1_000:  
                    assert fc(data) == sorted(data), f"{name} ошиблась на n={n}"
                time_s = timeit.timeit(lambda: fc(data), number=1)
                rows.append(("sorting", n, name, f"{time_s:.6f}"))
            else:
                rows.append(("sorting", n, name, ">60"))
    return rows
```

### `bench_search`

Замеряет линейный и бинарный поиск (10 000 запросов к списку из 100 000) и два решения Two Sum на n = 1 000 и 10 000.

```python
def bench_search() -> list[tuple[str, int, str, str]]:
    """Замеряет поиск (линейный и бинарный) и два решения Two Sum, возвращает список кортежей."""
    random.seed(42)
    rows = []
    n = 100_000
    data = [random.randint(-1_000_000, 1_000_000) for _ in range(n)]
    targets = [random.choice(data) for _ in range(10_000)]  

    time_ls = timeit.timeit(lambda: [linear_search(data, t) for t in targets], number=1)
    rows.append(("search", n, "linear_search", f"{time_ls:.6f}"))

    time_sort = timeit.timeit(lambda: sorted(data), number=10) / 10
    rows.append(("search", n, "sort_for_binary", f"{time_sort:.6f}"))

    sorted_data = sorted(data)
    time_bs = timeit.timeit(lambda: [binary_search(sorted_data, t) for t in targets], number=5) / 5
    rows.append(("search", n, "binary_search", f"{time_bs:.6f}"))

    for size in [1_000, 10_000]:
        data_ts = [random.randint(0, 10**9) for _ in range(size)]
        target = data_ts[-2] + data_ts[-1]
        assert two_sum_brute(data_ts, target) is not None
        assert two_sum_fast(data_ts, target) is not None

        time_b = timeit.timeit(lambda: two_sum_brute(data_ts, target), number=1)
        rows.append(("two_sum", size, "two_sum_brute", f"{time_b:.6f}"))
        time_f = timeit.timeit(lambda: two_sum_fast(data_ts, target), number=100) / 100
        rows.append(("two_sum", size, "two_sum_fast", f"{time_f:.6f}"))
    return rows
```

### `main`

Объединяет результаты, сохраняет их в `data/lab07/bench.csv` и выводит таблицу в консоль.

```python
def main():
    """Собирает все замеры, сохраняет в CSV и печатает таблицу в консоль."""
    header = ("task", "n", "impl", "seconds")
    rows = []
    rows.extend(bench_sorts())
    rows.extend(bench_search())

    os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
    write_csv(rows, CSV_PATH, header)

    print("Результаты бенчмарка:")
    print(f"{'Task':<10} | {'N':<8} | {'Impl':<18} | {'Seconds':<12}")
    print("-" * 56)
    for task, n, impl, sec in rows:
        print(f"{task:<10} | {n:<8} | {impl:<18} | {sec:<12}")
    print(f"Результаты сохранены в {CSV_PATH}")
```

### Результаты

Что вывелось в консоли:

![результаты бенчмарка](<../../images/lab07/results of bench.png>)

Те же данные в data: `data/lab07/bench.csv`:

![результаты в csv](<../../images/lab07/from csv.png>)



## Выводы

### Сортировки пузырьком, вставками, выбором и sorted
Алгоритмы с квадратичной сложностью (bubble_sort, insertion_sort, selection_sort) при росте объёма данных в 10 раз замедляются примерно в 100 раз. По моим замерам при переходе с 1 000 на 10 000 элементов время выросло примерно в 103–109 раз: с 0,0228 с до 2,3531 с у пузырька, с 0,0081 с до 0,8884 с у сортировки вставками и с 0,0084 с до 0,8728 с у сортировки выбором. Встроенный sorted() работает намного быстрее и масштабируется заметно мягче: с 10 000 до 100 000 элементов его время выросло примерно в 13,8 раза — с 0,000861 с до 0,011871 с. Уже на 10 000 элементов пузырёк медленнее sorted() более чем в 2 700 раз, а на 100 000 все три квадратичные сортировки в таблице ограничены значением >6


### Поиск, сортировка перед бинарным поиском и Two Sum

Бинарный поиск находит элемент за логарифмическое время, но требует заранее отсортированного массива. На списке из 100 000 элементов 10 000 линейных поисков заняли 8,4129 с (около 0,84 мс на один запрос), тогда как 10 000 бинарных поисков по готовому списку выполнились за 0,0111 с (около 1,11 мкс на запрос), а сама сортировка массива заняла 0,0118 с. Из-за затрат на сортировку (0,0118 с) при единичных запросах (примерно до 10–15 поисков) выгоднее обычный линейный перебор, но на серии из 10 000 запросов связка «сортировка + бинарный поиск» (0,0228 с суммарно) выигрывает примерно в 368 раз по сравнению с 8,4129 с у линейного поиска. Аналогичный выигрыш даёт словарь (two_sum_fast) вместо перебора пар (two_sum_brute) в задаче Two Sum: на n = 10 000 время сократилось с 1,5426 с до 0,0009 с (0,9 мс)

### Что показал `check.py`

Проведена 791 проверка. Все было отработано корректно. Никаких ошибок