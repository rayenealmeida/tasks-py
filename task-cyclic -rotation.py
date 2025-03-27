# rotacionar 

# Brute Solution 
# k= 3 
# A = [3, 8, 9, 7, 6]
# [6 3 8 9 7 ] k1
# [7 6 3 8 9] 2

# Better Solution
# k = 3
# A = [3, 8, 9, 7, 6] 4
# [9 7 6 3 8] 2
# (4+ k) % size A =2

def solution(A, K):
    N = len(A)
    # B = A.copy()
    B = [None] * N
    for i in range(0, N):
        B[(i+k) % N] = A[i]
    return B
    pass