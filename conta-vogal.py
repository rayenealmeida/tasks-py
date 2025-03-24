def conta_vogal():
    palavra = input("Digite uma palavra ou frase: ")
    vogais = 'aeiou'
    counter = 0

    for letra in palavra:
        if letra in vogais:
            counter +=1
    print(f"Quantidade de vogais de'{palavra}' é {counter}")

conta_vogal()