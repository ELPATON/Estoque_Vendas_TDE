"""
Módulo Pilha
------------
Responsável pelo histórico de vendas do turno/dia, permitindo desfazer
a última venda registrada.

Estrutura de dados usada: PILHA (LIFO - Last In, First Out).
Justificativa: um histórico de ações reversível é o caso de uso clássico
de pilha. A última venda feita é sempre a primeira que faz sentido
desfazer (ex.: operador digitou a quantidade errada, cliente desistiu
da compra). Por isso a remoção deve ocorrer sempre no topo, nunca em
posição arbitrária.

Regra respeitada: inserção (empilhar) e remoção (desempilhar) ocorrem
SOMENTE no topo da pilha, usando append() e pop() sem índice.

Complexidade:
    Empilhar (push): O(1)
    Desempilhar (pop): O(1)
    Consultar topo:    O(1)
"""

# Pilha representada como lista Python, mas usada SOMENTE com
# append() (empilhar) e pop() sem índice (desempilhar no topo).
historico_vendas = []


def empilhar_venda(venda):
    """Registra uma venda no topo do histórico (push)."""
    historico_vendas.append(venda)


def desempilhar_ultima_venda():
    """
    Remove e retorna a venda do topo da pilha (pop), ou seja,
    a última venda registrada. Retorna None se a pilha estiver vazia.
    """
    if pilha_vazia():
        return None
    return historico_vendas.pop()


def consultar_topo():
    """Consulta a última venda registrada sem removê-la."""
    if pilha_vazia():
        return None
    return historico_vendas[-1]


def pilha_vazia():
    """Verifica se o histórico de vendas está vazio."""
    return len(historico_vendas) == 0


def listar_historico():
    """
    Retorna o histórico completo, do mais recente para o mais antigo
    (ordem natural de leitura de uma pilha, do topo para a base).
    """
    return list(reversed(historico_vendas))