def first_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return -1

print(first_duplicate([1, 2, 3, 2, 4, 5]))  # Saída: 2
