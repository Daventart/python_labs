from io_txt_csv import write_csv

write_csv([("привет", 2), ("мир", 1)], "data/lab04/check.csv", header=("word", "count"))
print("записано")

try:
    write_csv([("a", 1), ("b",)], "data/lab04/bad.csv")
except ValueError as e:
    print("ошибка:", e)