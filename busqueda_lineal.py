import random

def busqueda_lineal(list, target):
    match = False

    for element in list: # O(n)
        if element == target:
            match = True
        break

    return match


if __name__ == '__main__':
    tamaño_de_lista = int(input('¿De qué tamaño será la lista?: '))
    object = int(input('¿Qué número quieres encontrar?: '))

    lista = [random.randint(0, 100) for i in range(tamaño_de_lista)]

    encontrado = busqueda_lineal(lista, object)
    print(lista)
    print(f'El elemento {object}, {"está" if encontrado else "no está"} en la lista.')