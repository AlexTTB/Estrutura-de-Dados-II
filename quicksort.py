import json

with open("listas.json", "r") as arquivo:
    listas = json.load(arquivo)

lista_10 = listas["10"]
lista_20 = listas["20"]
lista_1000 = listas["1000"]

def quick_sort(lista):
    comparacoes = 0
    movimentacoes = 0

    def ordenar(inicio, fim):
        nonlocal comparacoes, movimentacoes

        if inicio < fim:
            pivo = lista[fim]
            i = inicio - 1

            for j in range(inicio, fim):
                comparacoes += 1

                if lista[j] <= pivo:
                    i += 1

                    if i != j:
                        lista[i], lista[j] = lista[j], lista[i]
                        movimentacoes += 1

            if i + 1 != fim:
                lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
                movimentacoes += 1

            posicao_pivo = i + 1

            ordenar(inicio, posicao_pivo - 1)
            ordenar(posicao_pivo + 1, fim)

    ordenar(0, len(lista) - 1)

    return lista, comparacoes, movimentacoes


resultado, comparacoes, movimentos = quick_sort(lista_10.copy())

print("===== LISTA COM 10 ELEMENTOS =====")
print("Comparações:", comparacoes)
print("Movimentos:", movimentos)

resultado, comparacoes, movimentos = quick_sort(lista_20.copy())

print("===== LISTA COM 20 ELEMENTOS =====")
print("Comparações:", comparacoes)
print("Movimentos:", movimentos)

resultado, comparacoes, movimentos = quick_sort(lista_1000.copy())

print("===== LISTA COM 1000 ELEMENTOS =====")
print("Comparações:", comparacoes)
print("Movimentos:", movimentos)