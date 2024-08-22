def calcular_moda(lista):
    """Calcula a moda e a frequência de elementos em uma lista."""
    frequencias = {}

    # Contagem das frequências
    for elemento in lista:
        if elemento in frequencias:
            frequencias[elemento] += 1
        else:
            frequencias[elemento] = 1

    moda = []
    maior_frequencia = 0

    # Determinação da moda
    for elemento, frequencia in frequencias.items():
        if frequencia > maior_frequencia:
            moda = [elemento]
            maior_frequencia = frequencia
        elif frequencia == maior_frequencia:
            moda.append(elemento)

    return moda, maior_frequencia


# Entrada dos dados
lista = []
i = 1
while True:
    try:
        elem = int(input("Digite um elemento da lista (ou digite 'sair' para finalizar): "))
        lista.append(elem)
        i += 1
        if i > 10:  # Limite de 10 elementos
            break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro ou 'sair'.")

print("Lista:", lista)

# Resultados
moda, frequencia = calcular_moda(lista)
print("Moda:", moda)
print("Frequência:", frequencia)