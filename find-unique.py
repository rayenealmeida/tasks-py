def find_unique(A):
    unique = 0
    for num in A:
        unique ^= num #XOR 
    return unique
print(find_unique([1, 2, 2, 3, 1 ]))