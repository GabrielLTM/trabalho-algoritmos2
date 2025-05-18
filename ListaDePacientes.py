class Node:
    def __init__(self, nome, idade, registro_medico):
        self.nome = nome
        self.idade = idade
        self.registro_medico = registro_medico
        self.next = None


class ListaPaciente:
    def __init__(self):
        self.head = None

    def add_paciente(self, nome, idade, registro_medico):
        novo_paciente = Node(nome, idade, registro_medico)

        if self.head is None:
            self.head = novo_paciente
        else:
            paciente_atual = self.head
            while paciente_atual.next is not None:
                paciente_atual = paciente_atual.next
            paciente_atual.next = novo_paciente

    def busca_paciente(self, registro_medico):
        paciente_atual = self.head

        while paciente_atual is not None:
            if paciente_atual.registro_medico == registro_medico:
                return paciente_atual
            paciente_atual = paciente_atual.next

        return None

    def lista_pacientes(self):
        if self.head is None:
            print("A lista de pacientes está vazia.")
        else:
            paciente_atual = self.head
            while paciente_atual is not None:
                print(f"Nome: {paciente_atual.nome}, Idade: {paciente_atual.idade}, Prontuário: {paciente_atual.registro_medico}")
                paciente_atual = paciente_atual.next

def merge_sort(list):

    if list is None or list.next is None: # Caso base
        return list # Lista já ordenada

    # Dividindo a lista ao meio
    meio = split_list(list)

    # Ordenando as duas metades
    esquerda = merge_sort(meio[0])
    direita = merge_sort(meio[1])

    # Mesclando as listas ordenadas
    return merge(esquerda, direita) 


def split_list(list):
    meio = None # Inicializa o meio
    slow = list # Inicializa o ponteiro lento
    fast = list # Inicializa o ponteiro rápido

    while fast and fast.next: # Enquanto o ponteiro rápido não chegar ao final
        fast = fast.next.next # Avança duas posições
        meio = slow # Atualiza o meio
        slow = slow.next # Avança uma posição

    if meio: # Se o meio não for nulo
        meio.next = None # Divide a lista em duas

    return (list, slow) # Retorna as duas metades da lista


def merge(esquerda, direita): # Mescla duas listas encadeadas ordenadas 
    if not esquerda: # Se a lista da esquerda estiver vazia
        return direita  # retorna a lista da direita
    if not direita: # Se a lista da direita estiver vazia
        return esquerda # retorna a lista da esquerda

    if esquerda.registro_medico <= direita.registro_medico: # Compara os registros médicos
        resultado = esquerda # Se o registro médico da esquerda for menor ou igual ao da direita
        resultado.next = merge(esquerda.next, direita) # Chama recursivamente a função merge para o próximo nó
    else:
        resultado = direita # Se o registro médico da direita for menor
        resultado.next = merge(esquerda, direita.next) # Chama recursivamente a função merge para o próximo nó

    return resultado # retorna o resultado da mesclagem

pacientes = ListaPaciente()

pacientes.add_paciente("João", 30, "12345")
pacientes.add_paciente("Maria", 25, "67890")
pacientes.add_paciente("Pedro", 40, "54321")
pacientes.add_paciente("Ana", 35, "98765")
pacientes.add_paciente("Lucas", 28, "13579")

print("Lista de Pacientes:")
pacientes.lista_pacientes()

# Ordenando os pacientes com merge_sort
pacientes.head = merge_sort(pacientes.head)

# Listando os pacientes após a ordenação
print("\nLista de Pacientes Ordenada:")
pacientes.lista_pacientes()