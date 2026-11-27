import busca


# ======================================================================
# ÁRVORE AVL (implementada manualmente)
# A chave de cada nó é o código do produto e o valor é o dicionário do
# produto. A busca na árvore fica em busca.py (busca_avl).
# ======================================================================

class NoAVL:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.altura = 1
        self.esquerda = None
        self.direita = None


class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    # ---------- altura e fator de balanceamento ----------

    def _altura(self, no):
        if no is None:
            return 0
        return no.altura

    def _atualizar_altura(self, no):
        altura_esquerda = self._altura(no.esquerda)
        altura_direita = self._altura(no.direita)
        if altura_esquerda > altura_direita:
            no.altura = altura_esquerda + 1
        else:
            no.altura = altura_direita + 1

    def _fator_balanceamento(self, no):
        if no is None:
            return 0
        return self._altura(no.esquerda) - self._altura(no.direita)

    # ---------- rotações ----------

    def _rotacao_direita(self, no):
        novo_topo = no.esquerda
        no.esquerda = novo_topo.direita
        novo_topo.direita = no

        self._atualizar_altura(no)
        self._atualizar_altura(novo_topo)
        return novo_topo

    def _rotacao_esquerda(self, no):
        novo_topo = no.direita
        no.direita = novo_topo.esquerda
        novo_topo.esquerda = no

        self._atualizar_altura(no)
        self._atualizar_altura(novo_topo)
        return novo_topo

    # ---------- balanceamento ----------

    def _balancear(self, no):
        self._atualizar_altura(no)
        fator = self._fator_balanceamento(no)

        # Pesada para a esquerda
        if fator > 1:
            if self._fator_balanceamento(no.esquerda) < 0:
                # caso esquerda-direita: rotação dupla
                no.esquerda = self._rotacao_esquerda(no.esquerda)
            # caso esquerda-esquerda: rotação simples
            return self._rotacao_direita(no)

        # Pesada para a direita
        if fator < -1:
            if self._fator_balanceamento(no.direita) > 0:
                # caso direita-esquerda: rotação dupla
                no.direita = self._rotacao_direita(no.direita)
            # caso direita-direita: rotação simples
            return self._rotacao_esquerda(no)

        return no

    # ---------- inserção ----------

    def inserir(self, chave, valor):
        self.raiz, inserido = self._inserir(self.raiz, chave, valor)
        return inserido

    def _inserir(self, no, chave, valor):
        if no is None:
            return NoAVL(chave, valor), True

        if chave == no.chave:
            return no, False

        if chave < no.chave:
            no.esquerda, inserido = self._inserir(no.esquerda, chave, valor)
        else:
            no.direita, inserido = self._inserir(no.direita, chave, valor)

        if not inserido:
            return no, False

        return self._balancear(no), True

    # ---------- remoção ----------

    def remover(self, chave):
        self.raiz, removido = self._remover(self.raiz, chave)
        return removido

    def _menor_no(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no

    def _remover(self, no, chave):
        if no is None:
            return None, False

        if chave < no.chave:
            no.esquerda, removido = self._remover(no.esquerda, chave)
        elif chave > no.chave:
            no.direita, removido = self._remover(no.direita, chave)
        else:
            # Nó com no máximo um filho: o filho (ou None) ocupa o lugar dele
            if no.esquerda is None:
                return no.direita, True
            if no.direita is None:
                return no.esquerda, True

            # Nó com dois filhos: assume os dados do sucessor em ordem
            # (menor nó da direita) e o sucessor é removido da direita
            sucessor = self._menor_no(no.direita)
            no.chave = sucessor.chave
            no.valor = sucessor.valor
            no.direita, removido = self._remover(no.direita, sucessor.chave)

        if not removido:
            return no, False

        return self._balancear(no), True

    # ---------- travessias (retornam a lista de valores) ----------

    def em_ordem(self):
        resultado = []
        self._em_ordem(self.raiz, resultado)
        return resultado

    def _em_ordem(self, no, resultado):
        if no is None:
            return
        self._em_ordem(no.esquerda, resultado)
        resultado.append(no.valor)
        self._em_ordem(no.direita, resultado)

    def pre_ordem(self):
        resultado = []
        self._pre_ordem(self.raiz, resultado)
        return resultado

    def _pre_ordem(self, no, resultado):
        if no is None:
            return
        resultado.append(no.valor)
        self._pre_ordem(no.esquerda, resultado)
        self._pre_ordem(no.direita, resultado)

    def pos_ordem(self):
        resultado = []
        self._pos_ordem(self.raiz, resultado)
        return resultado

    def _pos_ordem(self, no, resultado):
        if no is None:
            return
        self._pos_ordem(no.esquerda, resultado)
        self._pos_ordem(no.direita, resultado)
        resultado.append(no.valor)


# ======================================================================
# ARMAZENAMENTO PRINCIPAL DOS PRODUTOS (árvore AVL, chave = código)
# ======================================================================

arvore_produtos = ArvoreAVL()


# ======================================================================
# CADASTRO DE PRODUTOS
# ======================================================================

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
    # A chave da árvore é o código já normalizado, igual ao que é gravado no cadastro
    return busca.busca_avl(arvore_produtos.raiz, str(codigo).strip())


def cadastrar_produto(codigo, nome, categoria, quantidade_estoque,
                       quantidade_minima, preco):
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

    arvore_produtos.inserir(produto["codigo"], produto)
    return True, f"Produto '{produto['nome']}' cadastrado com sucesso."


def consultar_produto(codigo):
    produto = buscar_produto_por_codigo(codigo)
    if produto is None:
        return False, f"Produto com código '{codigo}' não encontrado."
    return True, produto


def alterar_produto(codigo, nome=None, categoria=None,
                     quantidade_estoque=None, quantidade_minima=None,
                     preco=None):
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
    produto = buscar_produto_por_codigo(codigo)
    if produto is None:
        return False, f"Produto com código '{codigo}' não encontrado."

    arvore_produtos.remover(produto["codigo"])
    return True, f"Produto '{produto['nome']}' removido com sucesso."


# ======================================================================
# LISTAGENS (travessias da árvore)
# ======================================================================

def listar_produtos():
    # Travessia em ordem: produtos em ordem crescente de código
    return arvore_produtos.em_ordem()


def listar_produtos_pre_ordem():
    # Travessia pré-ordem: raiz, subárvore esquerda, subárvore direita
    return arvore_produtos.pre_ordem()


def listar_produtos_pos_ordem():
    # Travessia pós-ordem: subárvore esquerda, subárvore direita, raiz
    return arvore_produtos.pos_ordem()


def filtrar_produtos_por_categoria(categoria):
    todos = listar_produtos()
    resultado = []
    for i in range(len(todos)):
        if todos[i]["categoria"].lower() == categoria.lower():
            resultado.append(todos[i])
    return resultado
