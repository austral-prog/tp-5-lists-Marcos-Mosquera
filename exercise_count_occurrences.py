# Ejercicio 7: Contar ocurrencias de un elemento

def count_occurrences(lista, elemento):
    """
    Cuenta cuántas veces aparece un elemento en la lista.

    Args:
        lista: Una lista de elementos
        elemento: El elemento a buscar

    Returns:
        Un entero con la cantidad de veces que aparece el elemento
    """
    count=0
    for a in lista:
        if a == elemento:count+=1
    return count