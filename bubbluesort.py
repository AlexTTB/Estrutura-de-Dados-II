import json

with open("listas.json", "r") as arquivo:
    listas = json.load(arquivo)

lista_10 = listas["10"]
lista_20 = listas["20"]
lista_1000 = listas["1000"]

def bubble_sort(lista):
    comparacoes = 0
    movimentos = 0
    
    n = len(lista)

    for i in range(n):
        trocou = False

        for j in range(0, n - i - 1):
            comparacoes += 1

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                movimentos += 1
                trocou = True

        if not trocou:
            break

    return lista, comparacoes, movimentos

resultado, comparacoes, movimentos = bubble_sort(lista_10.copy())

print("===== LISTA COM 10 ELEMENTOS =====")
print("Comparações:", comparacoes)
print("Movimentos:", movimentos)

resultado, comparacoes, movimentos = bubble_sort(lista_20.copy())

print("===== LISTA COM 20 ELEMENTOS =====")
print("Comparações:", comparacoes)
print("Movimentos:", movimentos)

resultado, comparacoes, movimentos = bubble_sort(lista_1000.copy())

print("===== LISTA COM 1000 ELEMENTOS =====")
print("Comparações:", comparacoes)
print("Movimentos:", movimentos)