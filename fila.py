import heapq

fila = []
heapq.heappush(fila, (2, "Processo 2"))
heapq.heappush(fila, (1, "Processo 1"))
heapq.heappush(fila, (3, "Processo 3"))

print(heapq.heappop(fila))  # Saída: (1, 'Processo 1')

# heapq mantém a ordem dinâmica em O(log n), sendo mais eficiente que ordenar a cada inserção.
# menor valor primeiro