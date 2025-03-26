import heapq

numeros = [7, 2, 5, 8, 1, 3]
menores = heapq.nsmallest(3, numeros)
print(menores)  
