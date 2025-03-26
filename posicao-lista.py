import bisect

lista = [1, 3, 5, 7]
pos = bisect.bisect_left(lista, 4)
print(pos) # (posição onde 4 deveria entrar)
