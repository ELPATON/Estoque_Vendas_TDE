"""
Módulo Vendas
-------------
Autor: Charlison Almeida da Silva

Responsável pelo cadastro de vendas do mercadinho, integrando com o
estoque (produto.py) e com o histórico de vendas (pilha.py).

Estrutura de dados usada: LISTA.
Justificativa: assim como em produto.py, o cadastro de vendas precisa
de inserção, remoção e percurso livre (consultar, alterar, remover
qualquer venda, não só a última) — por isso lista, e não pilha. A
pilha (pilha.py) é usada só para o histórico/desfazer, que é uma
responsabilidade diferente (LIFO).

Cada venda é registrada como um dicionário:
    {
        "numero": int,              # identificador sequencial da venda
        "codigo_produto": str,
        "nome_produto": str,
        "quantidade": int,
        "preco_unitario": float,
        "valor_total": float,
    }
"""

import busca
import produto
import pilha

vendas = []
_proximo_numero = 1


def validar_dados_venda(codigo_produto, quantidade):
    if not codigo_produto or not str(codigo_produto).strip():
        return False, "Código do produto é obrigatório."

    produto_encontrado = produto.buscar_produto_por_codigo(codigo_produto)
    if produto_encontrado is None:
        return False, f"Produto com código '{codigo_produto}' não encontrado."

    try:
        quantidade = int(quantidade)
    except (ValueError, TypeError):
        return False, "Quantidade vendida deve ser um número inteiro."

    if quantidade <= 0:
        return False, "Quantidade vendida deve ser maior que zero."

    if quantidade > produto_encontrado["quantidade_estoque"]:
        return False, (
            f"Estoque insuficiente para '{produto_encontrado['nome']}'. "
            f"Disponível: {produto_encontrado['quantidade_estoque']}, "
            f"solicitado: {quantidade}."
        )

    return True, ""


def buscar_venda_por_numero(numero):
    return busca.busca_linear(vendas, "numero", numero)


def cadastrar_venda(codigo_produto, quantidade):
    global _proximo_numero

    valido, mensagem = validar_dados_venda(codigo_produto, quantidade)
    if not valido:
        return False, mensagem

    quantidade = int(quantidade)
    produto_vendido = produto.buscar_produto_por_codigo(codigo_produto)

    produto.alterar_produto(
        codigo_produto,
        quantidade_estoque=produto_vendido["quantidade_estoque"] - quantidade,
    )

    venda = {
        "numero": _proximo_numero,
        "codigo_produto": produto_vendido["codigo"],
        "nome_produto": produto_vendido["nome"],
        "quantidade": quantidade,
        "preco_unitario": produto_vendido["preco"],
        "valor_total": round(quantidade * produto_vendido["preco"], 2),
    }

    vendas.append(venda)
    pilha.empilhar_venda(venda)
    _proximo_numero += 1

    return True, (
        f"Venda #{venda['numero']} registrada: {quantidade}x "
        f"'{venda['nome_produto']}' — total R$ {venda['valor_total']:.2f}."
    )


def consultar_venda(numero):
    venda = buscar_venda_por_numero(numero)
    if venda is None:
        return False, f"Venda número {numero} não encontrada."
    return True, venda


def alterar_venda(numero, nova_quantidade):
    venda = buscar_venda_por_numero(numero)
    if venda is None:
        return False, f"Venda número {numero} não encontrada."

    try:
        nova_quantidade = int(nova_quantidade)
    except (ValueError, TypeError):
        return False, "Nova quantidade deve ser um número inteiro."

    if nova_quantidade <= 0:
        return False, "Nova quantidade deve ser maior que zero."

    produto_vendido = produto.buscar_produto_por_codigo(venda["codigo_produto"])
    if produto_vendido is None:
        return False, (
            f"Produto '{venda['codigo_produto']}' da venda não existe mais "
            "no estoque."
        )

    diferenca = nova_quantidade - venda["quantidade"]
    if diferenca > 0 and diferenca > produto_vendido["quantidade_estoque"]:
        return False, (
            f"Estoque insuficiente para aumentar a venda. Disponível: "
            f"{produto_vendido['quantidade_estoque']}, necessário: {diferenca}."
        )

    produto.alterar_produto(
        venda["codigo_produto"],
        quantidade_estoque=produto_vendido["quantidade_estoque"] - diferenca,
    )

    venda["quantidade"] = nova_quantidade
    venda["valor_total"] = round(nova_quantidade * venda["preco_unitario"], 2)

    return True, (
        f"Venda #{numero} alterada: nova quantidade {nova_quantidade}, "
        f"novo total R$ {venda['valor_total']:.2f}."
    )


def remover_venda(numero):
    venda = buscar_venda_por_numero(numero)
    if venda is None:
        return False, f"Venda número {numero} não encontrada."

    produto_vendido = produto.buscar_produto_por_codigo(venda["codigo_produto"])
    if produto_vendido is not None:
        produto.alterar_produto(
            venda["codigo_produto"],
            quantidade_estoque=(
                produto_vendido["quantidade_estoque"] + venda["quantidade"]
            ),
        )

    vendas.remove(venda)
    return True, f"Venda #{numero} removida e quantidade devolvida ao estoque."


def desfazer_ultima_venda():
    if pilha.pilha_vazia():
        return False, "Não há vendas no histórico para desfazer."

    venda = pilha.desempilhar_ultima_venda()
    venda_na_lista = buscar_venda_por_numero(venda["numero"])
    if venda_na_lista is None:
        return True, (
            f"Venda #{venda['numero']} removida do histórico (já não estava "
            "mais na lista de vendas)."
        )

    produto_vendido = produto.buscar_produto_por_codigo(venda["codigo_produto"])
    if produto_vendido is not None:
        produto.alterar_produto(
            venda["codigo_produto"],
            quantidade_estoque=(
                produto_vendido["quantidade_estoque"] + venda["quantidade"]
            ),
        )
    vendas.remove(venda_na_lista)

    return True, (
        f"Última venda desfeita: #{venda['numero']} — {venda['quantidade']}x "
        f"'{venda['nome_produto']}' devolvida ao estoque."
    )


def listar_vendas():
    return vendas