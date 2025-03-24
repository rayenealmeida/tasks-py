def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    
    return numero * fatorial(numero -1)
numero = int(input("Digite um número: "))
print(f"O fatorial do numero {numero} é: {fatorial(numero)}")




        
    
    