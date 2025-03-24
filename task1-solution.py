# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    num_set= set(A)
    menor = 1

    while menor in num_set:
        menor +=1
    
    return menor
    # Implement your solution here
    pass