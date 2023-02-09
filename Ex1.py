#ordenação de números em ordem decrescente

def ordenar(lista):
    indice_atual = 0
    while indice_atual < len(lista):
        menor_indice = indice_atual
        indice_proximo = indice_atual + 1
        while indice_proximo < len(lista):
            if lista[indice_proximo] > lista[menor_indice]:
                menor_indice = indice_proximo
            indice_proximo += 1
        lista[indice_atual], lista[menor_indice] = lista[menor_indice], lista[indice_atual]
        indice_atual += 1
    return lista
lista = [1,2, 4, 5, 7, 8, 9, 11, 13]
ordenar(lista)
print(lista)


