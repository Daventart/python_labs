import csv
import json
from pathlib import Path
from src.lib.io_helpers import ensure_parent_dir

def json_to_csv(json_path: str, csv_path: str) -> None:


    src = Path(json_path)
    dst = Path(csv_path)


    if not src.exists():
        raise FileNotFoundError(f'JSON файл не найден {src}')
    if src.suffix.lower() != '.json':
        raise ValueError(f'Ожидался JSON, получен {src.name}')
    if dst.suffix.lower() != '.csv':
        raise ValueError(f'Ожидался файл CSV, получен {dst.name}')
    
    with src.open("r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Некорректный или пустой JSON: {e}") from e
        if not isinstance(data, list) or not data:
            raise ValueError('Пустой JSON или неподдерживаю структуру')
        if not all(isinstance(item, dict) for item in data):
            raise ValueError('Все элементы Json списка должны быть словарями')

        fieldnames: list[str] = []
        for item in data:
            for key in item:
                if key in item:
                    if key not in fieldnames:
                        fieldnames.append(key)
        ensure_parent_dir(dst)
        with dst.open('w', newline='', encoding= 'utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    src = Path(csv_path)
    dst = Path(json_path)

    if not src.exists():
        raise FileNotFoundError(f"CSV-файл не найден: {src}")
    if src.suffix.lower() != ".csv":
        raise ValueError(f"Ожидался файл .csv, получен: {src.name}")
    if dst.suffix.lower() != ".json":
        raise ValueError(f"Ожидался файл .json, получен: {dst.name}")

    with src.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV пустой или без заголовка")
        rows = list(reader)

    if not rows:
        raise ValueError("CSV не содержит строк данных")

    ensure_parent_dir(dst)
    with dst.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
    csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")
    print("JSON -> CSV и CSV -> JSON: готово")