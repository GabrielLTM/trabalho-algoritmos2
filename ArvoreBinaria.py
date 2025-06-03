class No:
    def __init__(self, valor):
        self.valor = valor
        self.filhos = []

    def adicionar_filho(self, filho):
        self.filhos.append(filho)

class Arvore:
    def __init__(self, valor_raiz):
        self.raiz = No(valor_raiz)

    def buscar(self, valor, no_atual=None):
        if no_atual is None:
            no_atual = self.raiz

        if no_atual.valor == valor:
            return no_atual

        for filho in no_atual.filhos:
            resultado = self.buscar(valor, filho)
            if resultado:
                return resultado

        return None

    def adicionar_no(self, valor, valor_pai=None):
        novo_no = No(valor)
        if valor_pai is None:
            raise Exception("A árvore já tem uma raiz.")
        pai = self.buscar(valor_pai)
        if pai:
            pai.adicionar_filho(novo_no)
        else:
            raise ValueError(f"Pai com valor {valor_pai} não encontrado.")

    def imprimir(self, no=None, nivel=0):
        if no is None:
            no = self.raiz
        print("  " * nivel + str(no.valor))
        for filho in no.filhos:
            self.imprimir(filho, nivel + 1)
            
            
    
    def buscar_com_pai(self, valor, no=None, pai=None):
        if no is None:
            no = self.raiz

        if no.valor == valor:
            return no, pai

        for filho in no.filhos:
            resultado = self.buscar_com_pai(valor, filho, no)
            if resultado[0] is not None:
                return resultado

        return None, None

    def remover_no(self, valor):
        no_remover, pai = self.buscar_com_pai(valor)

        if no_remover is None:
            print(f"Nó com valor '{valor}' não encontrado.")
            return

        if pai is None:
            print("Não é possível remover a raiz.")
            return

        pai.filhos.remove(no_remover)
        print(f"Nó '{valor}' e seus filhos foram removidos com sucesso.")
            

# Exemplo de uso

teste = Arvore("Raiz")
teste.adicionar_no("Filho 1", "Raiz")
teste.adicionar_no("Filho 2", "Raiz")
teste.adicionar_no("Filho 1.1", "Filho 1")
teste.adicionar_no("Filho 1.2", "Filho 1")

teste.imprimir()

teste.remover_no("Filho 1")
teste.imprimir()