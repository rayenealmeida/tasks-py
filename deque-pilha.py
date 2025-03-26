# Criar uma pilha eficiente (LIFO - Last In, First Out)
from collections import deque

pilha = deque()
pilha.append("X")
pilha.append("Y")
pilha.append("Z")
print(pilha.pop()) 
