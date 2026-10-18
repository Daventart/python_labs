def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    else: 
        text = text.lower()
    if yo2e:
        text = text.replace('Ё' ,'Е').replace('ё','е')
    text = ' '.join(text.split())

    return text
# print(f'normalize("ПрИвЕт\nМИр\t") ->', normalize("ПрИвЕт\nМИр\t"))
# print(f'normalize("ёжик, Ёлка" (yo2e=True)) ->', normalize("ёжик, Ёлка", yo2e=True))
# print(f'normalize("Hello\r\nWorld") ->', normalize("Hello\r\nWorld"))
# print(f'normalize("  двойные   пробелы  ") ->', normalize("  двойные   пробелы  "))

import re
def tokenize(text: str) -> list[str]:
    matches = re.finditer(r'\w+(-\w+)*', text)
    newtext = []
    for alphas in matches:
        newtext.append(alphas.group())
    return newtext
#print(f'tokenize("привет мир") ->', tokenize("привет мир"))
#print(f'tokenize("hello,world!!!")) ->', tokenize("hello,world!!!"))
#print(f'tokenize("2025 год") ->', tokenize("2025 год"))
#print(f'tokenize("по-настоящему круто") ->', tokenize("по-настоящему круто"))
#print(f'tokenize(emoji 😀 не слово") ->', tokenize("emoji 😀 не слово"))

def count_freq(tokens: list[str]) -> dict[str, int]:
    word_counts = {}

    for token in tokens:
        if token in word_counts:
            word_counts[token] += 1
        else:
            word_counts[token] = 1

    return dict(sorted(word_counts.items()))
#print(f'count_freq["a","b","a","c","b","a"] ->', count_freq(["a","b","a","c","b","a"]))
#print(f'count_freq["bb","aa","bb","aa","cc"] ->', count_freq(["bb","aa","bb","aa","cc"]))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    freqs = sorted(freq.items(), key = lambda x: (-x[1], x[0]))[:n]
    return freqs

#freq1 = {"a": 3, "b": 2, "c": 1}
#freq2 = {"aa": 2, "bb": 2, "cc": 1}
#print(f'top_n({freq1}, n=2) ->', top_n(freq1, n=2))
#print(f'top_n({freq2}, n=2) ->', top_n(freq2, n=2))