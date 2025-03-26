# soma rápida de um intervalo em um array 
def prefix_sum(A):
    prefix = [0] * (len(A) + 1)
    for i in range(len(A)):
        prefix[i + 1] = prefix[i] + A[i]
    return prefix

arr = [2, 3, 7, 5]
print(prefix_sum(arr))  # [0, 2, 5, 12, 17]
