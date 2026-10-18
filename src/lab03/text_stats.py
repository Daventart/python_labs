import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lib.text import normalize, tokenize, count_freq, top_n


def main() -> None:
    sys.stdin.reconfigure(encoding="utf-8")
    raw_text = sys.stdin.read()  

    tokens = tokenize(normalize(raw_text))
    freq = count_freq(tokens)
    print(tokens)
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top_n(freq, n=5):
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()









#Set-Alias python "C:\Users\alexl\.local\bin\python3.14.exe"
#[Console]::InputEncoding = [Text.Encoding]::UTF8
#$OutputEncoding = [Text.Encoding]::UTF8
#echo "Привет, мир! Привет!!!" | python src/lab03/text_stats.py