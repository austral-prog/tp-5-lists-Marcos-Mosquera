# Ejercicio 12: Manipular lista de listas

def list_of_lists(lista_de_listas):
    """
    Modifica una lista de 3 listas internas:
    - Primera lista: solo los primeros 2 elementos
    - Segunda lista: elementos entre el segundo y cuarto
    - Tercera lista: solo los últimos 2 elementos

    Args:
        lista_de_listas: Una lista que contiene 3 listas

    Returns:
        La lista de listas modificada según las reglas
    """
    final=[]
    primera=[]
    segunda=[]
    tercera=[]
    if lista_de_listas[0]!=[]:
        if len(lista_de_listas[0])>2:
            primera = [lista_de_listas[0][0],lista_de_listas[0][1]]
        else:
            primera = lista_de_listas[0]
    else:pass


    if len(lista_de_listas[1])>=2:
        if len(lista_de_listas[1])>=4:
            segunda = [lista_de_listas[1][1],lista_de_listas[1][2],lista_de_listas[1][3]]
        elif len(lista_de_listas[1])<=3:
            segunda = lista_de_listas[1][1::]
    else:pass


    if lista_de_listas[2]!=[]:
        if len(lista_de_listas[2])>=2:
            tercera = [lista_de_listas[2][-2],lista_de_listas[2][-1]]
        else:
            tercera = lista_de_listas[2]
    else:pass

    final = [primera,segunda,tercera]
    return final