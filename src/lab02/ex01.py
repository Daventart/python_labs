def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("список пуст")
    low = float('inf')
    high = float('-inf')
    for numbers in nums:
        if numbers < low:
            low = numbers
        if numbers > high:
            high = numbers
    return (low, high)


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    items = list(set(nums))
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        while j >= 0 and items[j] > key:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key
    return items


def flatten(mat: list[list | tuple]) -> list:
    a = []
    for row in mat:
        if type(row) != list and type(row) != tuple:
            raise TypeError("Строка должна быть списком или кортежем")
        for x in row:
            a.append(x)

    return a

#тест кейс

if __name__ == "__main__":
    print("min_max")
    print("[3, -1, 5, 5, 0] →", min_max([3, -1, 5, 5, 0]))
    print("[42] →", min_max([42]))
    print("[-5, -2, -9] →", min_max([-5, -2, -9]))
    print("[1.5, 2, 2.0, -3.1] →", min_max([1.5, 2, 2.0, -3.1]))
    print("[] →", min_max([]))

""""
if __name__ == "__main__":
    print("unique_sorted")
    print("[3, 1, 2, 1, 3] →", unique_sorted([3, 1, 2, 1, 3]))
    print("[] →", unique_sorted([]))
    print("[-1, -1, 0, 2, 2] →", unique_sorted([-1, -1, 0, 2, 2]))
    print("[1.0, 1, 2.5, 2.5, 0] →", unique_sorted([1.0, 1, 2.5, 2.5, 0]))
"""
""""
if __name__ == "__main__":
    print("flatten")
    print("[[1, 2], [3, 4]] →", flatten([[1, 2], [3, 4]]))
    print("[[1, 2], (3, 4, 5)] →", flatten([[1, 2], (3, 4, 5)]))
    print("[[1], [], [2, 3]] →", flatten([[1], [], [2, 3]]))
    print("[[1, 2] , "'ab'"]→", flatten([[1, 2], "ab"]))
"""