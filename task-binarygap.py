# read the sequence
# increment a counter variable for each zero digit
# Reset my counter every time I reach a "1" digit
# Compare zero counter with the current maxximum value

def solution(N):
    N = bin(N) [2:]
    b=0
    maxb = 0
    for k in N:
        if int(k) == 0:
            b+=1
        elif int(k) == 1:
            maxb=max(b,maxb)
            b=0

    return maxb
