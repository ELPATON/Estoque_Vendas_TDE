
import busca

produtos = []


def validar_dados_produto(codigo, nome, categoria, quantidade_estoque,
                           quantidade_minima, preco):
    
    if not codigo or not str(codigo).strip():
        return False, "Código do produto é obrigatório."
    if not nome or not str(nome).strip():
        return False, "Nome do produto é obrigatório."
    if not categoria or not str(categoria).strip():
        return False, "Categoria do produto é obrigatória."

    try:
        quantidade_estoque = int(quantidade_estoque)
        quantidade_minima = int(quantidade_minima)
    except (ValueError, TypeError):
        return False, "Quantidade em estoque e quantidade mínima devem ser números inteiros."

    if quantidade_estoque < 0:
        return False, "Quantidade em estoque não pode ser negativa."
    if quantidade_minima < 0:
        return False, "Quantidade mínima não pode ser negativa."

    try:
        preco = float(preco)
    except (ValueError, TypeError):
        return False, "Preço deve ser um número válido."

    if preco <= 0:
        return False, "Preço deve ser maior que zero."

    return True, ""


def buscar_produto_por_codigo(codigo):
    """
    Busca produto por código, usando o algoritmo de busca linear
    manual implementado em busca.py (evita duplicar a lógica de
    busca em cada módulo).

    Complexidade:
        Melhor caso: O(1)  -> produto é o primeiro da lista
        Pior caso:   O(n)  -> produto é o último ou não existe, percorre tudo
        Caso médio:  O(n)

    Retorna o dicionário do produto se encontrado, ou None.
    """
    return busca.busca_linear(produtos, "codigo", codigo)


def cadastrar_produto(codigo, nome, categoria, quantidade_estoque,
                       quantidade_minima, preco):
    """
    Cadastra um novo produto na lista, se os dados forem válidos
    e o código ainda não existir.
    """
    valido, mensagem = validar_dados_produto(
        codigo, nome, categoria, quantidade_estoque, quantidade_minima, preco
    )
    if not valido:
        return False, mensagem

    if buscar_produto_por_codigo(codigo) is not None:
        return False, f"Já existe um produto cadastrado com o código '{codigo}'."

    produto = {
        "codigo": str(codigo).strip(),
        "nome": str(nome).strip(),
        "categoria": str(categoria).strip(),
        "quantidade_estoque": int(quantidade_estoque),
        "quantidade_minima": int(quantidade_minima),
        "preco": float(preco),
    }

    produtos.append(produto)
    return True, f"Produto '{produto['nome']}' cadastrado com sucesso."


def consultar_produto(codigo):
    """Consulta um produto pelo código, usando a busca manual."""
    produto = buscar_produto_por_codigo(codigo)
    if produto is None:
        return False, f"Produto com código '{codigo}' não encontrado."
    return True, produto


def alterar_produto(codigo, nome=None, categoria=None,
                     quantidade_estoque=None, quantidade_minima=None,
                     preco=None):
    """
    Altera os dados de um produto existente. Só altera os campos
    que forem informados (diferentes de None).
    """
    produto = buscar_produto_por_codigo(codigo)
    if produto is None:
        return False, f"Produto com código '{codigo}' não encontrado."

    novo_nome = nome if nome is not None else produto["nome"]
    novo_categoria = categoria if categoria is not None else produto["categoria"]
    nova_qtd_estoque = (quantidade_estoque if quantidade_estoque is not None
                         else produto["quantidade_estoque"])
    nova_qtd_minima = (quantidade_minima if quantidade_minima is not None
                        else produto["quantidade_minima"])
    novo_preco = preco if preco is not None else produto["preco"]

    valido, mensagem = validar_dados_produto(
        codigo, novo_nome, novo_categoria, nova_qtd_estoque,
        nova_qtd_minima, novo_preco
    )
    if not valido:
        return False, mensagem

    produto["nome"] = str(novo_nome).strip()
    produto["categoria"] = str(novo_categoria).strip()
    produto["quantidade_estoque"] = int(nova_qtd_estoque)
    produto["quantidade_minima"] = int(nova_qtd_minima)
    produto["preco"] = float(novo_preco)

    return True, f"Produto '{produto['nome']}' alterado com sucesso."


def remover_produto(codigo):
    """Remove um produto do cadastro pelo código."""
    produto = buscar_produto_por_codigo(codigo)
    if produto is None:
        return False, f"Produto com código '{codigo}' não encontrado."

    produtos.remove(produto)
    return True, f"Produto '{produto['nome']}' removido com sucesso."


def listar_produtos():
    """Retorna a lista completa de produtos (percurso simples)."""
    return produtos


def filtrar_produtos_por_categoria(categoria):
    """
    Filtra produtos por categoria, percorrendo a lista manualmente
    (sem usar filter()).
    """
    resultado = []
    for i in range(len(produtos)):
        if produtos[i]["categoria"].lower() == categoria.lower():
            resultado.append(produtos[i])
    return resultado