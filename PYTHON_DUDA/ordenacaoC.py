#Ordenação customizada

def ordenar_por_letras(item):
    return len(item)

lista = ['Ana', 'Beatriz', 'Carla', 'Daniela', 'Elizabeth']

lista_ordenada = sorted(lista, key = ordenar_por_letras)

print(lista_ordenada)