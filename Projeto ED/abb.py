class NoExisteError(Exception):
    pass


class ResultadoBusca:

    def __init__(self, existe, nivel):
        self.existe = existe
        self.nivel = nivel


class Node:

    def __init__(self, data):
        self.dado = data
        self.filho_esquerda = None
        self.filho_direita = None

    def __repr__(self):
        return f'Node(dado={self.dado})'

    def add_esquerda(self, dado):
        if self.tem_filho_esquerda:
            raise NoExisteError()
        
        self.filho_esquerda = Node(dado)
        
    def add_direita(self, dado):
        if self.tem_filho_direita:
            raise NoExisteError()
        
        self.filho_direita = Node(dado)
        
    @property
    def tem_filho_esquerda(self) -> bool:
        return self.filho_esquerda is not None

    @property
    def tem_filho_direita(self) -> bool:
        return self.filho_direita is not None
    
    @property
    def eh_folha(self) -> bool:
        return not self.tem_filho_esquerda and not self.tem_filho_direita



class Arvore:

    def __init__(self):
        self.raiz: Node|None = None

    def esta_vazia(self) -> bool:
        return self.raiz is None

    def get_no_raiz(self) -> Node|None:
        return self.raiz

    def carregar_arvore(self):
        arquivo = open('dicionario.txt', 'r')
        for linha in arquivo:
            self.raiz = linha.readline()
            linha = Node(linha)
            
        

    def add(self, valor: int) -> None:
        self.raiz = self._add(self.raiz, valor)
        
    def _add(self, node: Node, dado: int):
        if node is None:
            return Node(dado)
        elif dado < node.dado:
            node.filho_esquerda = self._add(node.filho_esquerda, dado)
        else:
            node.filho_direita = self._add(node.filho_direita, dado)
        return node

    def imprimir(self):
        self._imprimir_em_ordem(self.raiz)
        print()

    def _imprimir_pre_ordem(self, node: Node):
        if node is None:
            return

        print(node.dado, end=" ")
        self._imprimir_pre_ordem(node.filho_esquerda)
        self._imprimir_pre_ordem(node.filho_direita)
        
    def _imprimir_em_ordem(self, node: Node):
        if node is None:
            return

        self._imprimir_em_ordem(node.filho_esquerda)
        print(node.dado, end=" ")
        self._imprimir_em_ordem(node.filho_direita)

    def _imprimir_pos_ordem(self, node: Node):
        if node is None:
            return

        self._imprimir_pos_ordem(node.filho_esquerda)
        self._imprimir_pos_ordem(node.filho_direita)
        print(node.dado, end=" ")

    def get_quantidade(self) -> int:
        return self._get_quantidade(self.raiz)

    def _get_quantidade(self, node: Node) -> int:
        if node is None:
            return 0

        return 1 + self._get_quantidade(node.filho_esquerda) + self._get_quantidade(node.filho_direita)

    def get_altura(self) -> int:
        return self._get_altura(self.raiz)

    def _get_altura(self, node: Node) -> int:
        if node is None:
            return 0

        alt_esquerda = self._get_altura(node.filho_esquerda)
        alt_direita = self._get_altura(node.filho_direita)
        return 1 + max(alt_esquerda, alt_direita)

    def busca(self, valor: int) -> ResultadoBusca:
        return self._busca(self.raiz, valor, nivel=1)

    def _busca(self, node: Node, valor: int, nivel: int) -> ResultadoBusca:
        if node is None:
            return ResultadoBusca(existe=False, nivel=nivel)
        
        if valor == node.dado:
            return ResultadoBusca(existe=True, nivel=nivel)
        elif valor < node.dado:
            return self._busca(node.filho_esquerda, valor, nivel=nivel+1)
        else:
            return self._busca(node.filho_direita, valor, nivel=nivel+1)

    def nos_folhas(self) -> int:
        return self._nos_folhas(self.raiz)

    def _nos_folhas(self, node: Node) -> int:
        if node is None:
            return 0
        if node.eh_folha:
            return 1
        else:
            return self._nos_folhas(node.filho_esquerda) + self._nos_folhas(node.filho_direita)

    
    def no_menor_valor(self, node: Node):
        atual = node
        while atual.tem_filho_esquerda:
            atual = atual.filho_esquerda
        return atual


    def remover(self, valor: int):
        return self._remover(self.raiz, valor)

    def _remover(self, node: Node, valor: int):
        if node is None:
            return node
        
        if valor < node.dado:
            node.filho_esquerda = self._remover(node.filho_esquerda, valor)
        elif valor > node.dado:
            node.filho_direita = self._remover(node.filho_direta, valor)
        else:
            if not node.tem_filho_esquerda:
                return node.filho_direita
            elif not node.tem_filho_direita:
                return node.filho_esquerda
            else:
                substituto = self.no_menor_valor(node.filho_direita)
                node.dado = substituto.dado
                node.filho_direita = self._remover(
                    node.filho_direita,
                    substituto.dado
                )
        return node

if __name__ == '__main__':
