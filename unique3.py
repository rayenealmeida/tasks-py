def find_unique(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    for num, count in freq.items():
        if count == 1:
            return num

print(find_unique([4, 3, 2, 4, 1, 3, 2]))  
