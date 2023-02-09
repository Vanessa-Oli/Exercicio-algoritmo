lista = []

def ordenar(lista):
    indice_atual = 0
    while indice_atual < len(lista):
        menor_indice = indice_atual
        indice_proximo = indice_atual + 1
        while indice_proximo < len(lista):
            if lista[indice_proximo] < lista[menor_indice]:
                menor_indice = indice_proximo
            indice_proximo += 1
        lista[indice_atual], lista[menor_indice] = lista[menor_indice], lista[indice_atual]
        indice_atual += 1
    return lista

for n in range(5):
    num = str(input('Digite uma frunta: '))
    lista.append(num)
    ordenar(lista)
    print(lista)