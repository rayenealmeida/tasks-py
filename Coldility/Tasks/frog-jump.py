# easy

# [] [x] [] [] [] [] [y] []
# d/D = 6/4 = 1 (int)

def solution(X, Y,  D):
    v = (Y - X) // D
    if X+v*D >= Y:
        return v
    else:
        return v+1
    pass

# Better but with import
import math

def solution(X, Y, D):
    return math.ceil((Y - X) / D) 
