def busca_linear(lista, campo, valor_procurado):
    if lista is None:
        return None

    for item in lista:
        if item.get(campo) == valor_procurado:
            return item
    return None


def busca_linear_indice(lista, campo, valor_procurado):
    if lista is None:
        return -1

    for indice in range(len(lista)):
        if lista[indice].get(campo) == valor_procurado:
            return indice
    return -1


def busca_linear_string(lista, campo, valor_procurado, ignorar_maiusculas=True):
    if lista is None:
        return None

    valor = str(valor_procurado)
    for item in lista:
        atual = str(item.get(campo, ""))
        if ignorar_maiusculas:
            atual = atual.lower()
            valor = valor.lower()
        if atual == valor:
            return item
    return None