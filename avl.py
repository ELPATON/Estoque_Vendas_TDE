"""
Módulo AVL
----------
Árvore AVL implementada manualmente (sem bibliotecas), usada como
armazenamento principal de Produtos (chave = código) e Vendas
(chave = número da venda).

Complexidade (n = número de nós, a altura é sempre O(log n)):
    Inserção: O(log n)
    Remoção:  O(log n)
    Busca:    O(log n)   (ver busca.busca_avl)
    Travessias (em ordem, pré-ordem, pós-ordem): O(n)
"""

import busca


class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1


def altura(no):
    if no is None:
        return 0
    return no.altura


def _atualizar_altura(no):
    altura_esq = altura(no.esquerda)
    altura_dir = altura(no.direita)
    if altura_esq > altura_dir:
        no.altura = altura_esq + 1
    else:
        no.altura = altura_dir + 1


def fator_balanceamento(no):
    if no is None:
        return 0
    return altura(no.esquerda) - altura(no.direita)


def rotacao_direita(y):
    x = y.esquerda
    subarvore = x.direita

    x.direita = y
    y.esquerda = subarvore

    _atualizar_altura(y)
    _atualizar_altura(x)
    return x


def rotacao_esquerda(x):
    y = x.direita
    subarvore = y.esquerda

    y.esquerda = x
    x.direita = subarvore

    _atualizar_altura(x)
    _atualizar_altura(y)
    return y


def balancear(no):
    """Atualiza a altura do nó e aplica as rotações necessárias (LL, RR, LR, RL)."""
    _atualizar_altura(no)
    fator = fator_balanceamento(no)

    if fator > 1:
        if fator_balanceamento(no.esquerda) < 0:
            no.esquerda = rotacao_esquerda(no.esquerda)      # caso LR
        return rotacao_direita(no)                            # caso LL

    if fator < -1:
        if fator_balanceamento(no.direita) > 0:
            no.direita = rotacao_direita(no.direita)          # caso RL
        return rotacao_esquerda(no)                           # caso RR

    return no


def _inserir(no, chave, valor):
    if no is None:
        return No(chave, valor)

    if chave < no.chave:
        no.esquerda = _inserir(no.esquerda, chave, valor)
    else:
        no.direita = _inserir(no.direita, chave, valor)

    return balancear(no)


def _remover(no, chave):
    if no is None:
        return None

    if chave < no.chave:
        no.esquerda = _remover(no.esquerda, chave)
    elif chave > no.chave:
        no.direita = _remover(no.direita, chave)
    else:
        if no.esquerda is None:
            return no.direita
        if no.direita is None:
            return no.esquerda

        # Dois filhos: troca pelo sucessor em ordem (menor da subárvore direita)
        sucessor = no.direita
        while sucessor.esquerda is not None:
            sucessor = sucessor.esquerda
        no.chave = sucessor.chave
        no.valor = sucessor.valor
        no.direita = _remover(no.direita, sucessor.chave)

    return balancear(no)


def _em_ordem(no, nivel, resultado):
    if no is None:
        return
    _em_ordem(no.esquerda, nivel + 1, resultado)
    resultado.append((nivel, no.valor))
    _em_ordem(no.direita, nivel + 1, resultado)


def _pre_ordem(no, nivel, resultado):
    if no is None:
        return
    resultado.append((nivel, no.valor))
    _pre_ordem(no.esquerda, nivel + 1, resultado)
    _pre_ordem(no.direita, nivel + 1, resultado)


def _pos_ordem(no, nivel, resultado):
    if no is None:
        return
    _pos_ordem(no.esquerda, nivel + 1, resultado)
    _pos_ordem(no.direita, nivel + 1, resultado)
    resultado.append((nivel, no.valor))


class ArvoreAVL:
    def __init__(self):
        self.raiz = None
        self.quantidade = 0

    def buscar(self, chave):
        return busca.busca_avl(self.raiz, chave)

    def inserir(self, chave, valor):
        """Retorna False (sem inserir) se a chave já existir."""
        if self.buscar(chave) is not None:
            return False
        self.raiz = _inserir(self.raiz, chave, valor)
        self.quantidade += 1
        return True

    def remover(self, chave):
        """Retorna False se a chave não existir."""
        if self.buscar(chave) is None:
            return False
        self.raiz = _remover(self.raiz, chave)
        self.quantidade -= 1
        return True

    def altura(self):
        return altura(self.raiz)

    # Cada travessia devolve uma lista de tuplas (nivel, valor).
    def em_ordem(self):
        resultado = []
        _em_ordem(self.raiz, 0, resultado)
        return resultado

    def pre_ordem(self):
        resultado = []
        _pre_ordem(self.raiz, 0, resultado)
        return resultado

    def pos_ordem(self):
        resultado = []
        _pos_ordem(self.raiz, 0, resultado)
        return resultado

    def valores_em_ordem(self):
        """Só os valores, em ordem crescente de chave."""
        valores = []
        for _, valor in self.em_ordem():
            valores.append(valor)
        return valores
