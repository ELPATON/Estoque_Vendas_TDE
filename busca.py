
def busca_linear(lista, campo, valor_procurado):
   
    for i in range(len(lista)):
        if lista[i][campo] == valor_procurado:
            return lista[i]
    return None


def busca_linear_indice(lista, campo, valor_procurado):
   
    for i in range(len(lista)):
        if lista[i][campo] == valor_procurado:
            return i
    return -1