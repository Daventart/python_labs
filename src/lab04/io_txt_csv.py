"""Ввод/вывод для ЛР4: чтение текста и запись CSV."""

import csv
from typing import Iterable, Sequence
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    return p.read_text(encoding=encoding)
#print(repr(read_text('data/lab04/input.txt', encoding ="cp1251")))

def ensure_parent_dir(path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)

def write_csv(
        rows:Iterable[Sequence],
        path: str | Path,
        header: tuple[str, ...]| None = None,
) -> None:
    rows = list(rows)

    if header is not None:
        expected = len(header)
    elif rows:
        expected = len(rows[0])
    else:
        expected = None

    for number, row in enumerate(rows, start=1):
        if len(row) != expected:
            raise ValueError(
                f'Строка {number} содержит {len(row)} значений, ожидалось {expected}'
            )
    ensure_parent_dir(path)
    with Path(path).open('w', newline = '', encoding='utf-8') as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)