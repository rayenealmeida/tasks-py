
# Criar uma fila eficiente (FIFO - First In, First Out)

from collections import deque

fila = deque()
fila.append("A")
fila.append("B")
fila.append("C")
print(fila.popleft())  
