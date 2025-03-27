# Odd Occurrences in array
# [9, 3, 9, 3, 9, *7*, 9] -> 7

# Efficient Solution
# sort
# test equality between consecutive elements
# increment index by 2

# Slow
def solution(A):
    A.sort()
    A.append(-1)
    for i in range(0, len(A),2):
        if A[i] != A[i+1]:
            return A[i]
pass

# Better but not efficient solution
def solution(A):
    if len(A)==1:
        return A[0]
    A.sort()
    for i in range (0, len(A)-1,2):
        if A[i] != A[i+1]:
            return A[i]
        return A[-1]

# The real efficient solution 
def solution(A):
    result = 0
    for num in A:
        result ^= num
    return result
