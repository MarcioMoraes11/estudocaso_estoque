# Controle de estoque estudo de caso UniFecaf
# Este script permite gerenciar o estoque de uma loja, com funcionalidades para adicionar, atualizar, excluir e visualizar produtos.

estoque = {} 

# Função para adicionar produto ao estoque
# A função adiciona um produto ao estoque, verificando se o nome já existe

def adicionar_produto():
  
    nome = input("Nome do produto: ").strip().capitalize()
    if nome in estoque:
        print(f"Opa, {nome} já está na lista.")
        return 

    try:
        preco = float(input(f"Preço de {nome}: R$ "))
        qtd = int(input(f"Quantidade inicial de {nome}: "))

        # Não permitir valores menores ou iguais a zero.
        if preco <= 0 or qtd <= 0:
            print("Erro: Preço e quantidade não podem ser menores ou iguais a zero.")
            return

        estoque[nome] = {'preco': preco, 'quantidade': qtd}
        print(f"{nome} adicionado ao estoque!")

    except ValueError:
        print("Erro: Preço e quantidade precisam ser números.")
# Função para atualizar produto no estoque
def atualizar_produto():
    nome = input("Qual produto quer atualizar? ").strip().capitalize()
    if nome not in estoque:
        print("Produto não encontrado.")
        return

    try:
        # Solicitar novo preço e quantidade, com opção de deixar em branco para não alterar o preço anterior do produto
        print(f"(Deixe em branco para não alterar)")
        novo_preco_str = input(f"Novo preço (atual: R${estoque[nome]['preco']:.2f}): R$ ")
        nova_qtd_str = input(f"Nova quantidade (atual: {estoque[nome]['quantidade']}): ")

        if novo_preco_str:
            novo_preco = float(novo_preco_str)
            if novo_preco <= 0:
                print("Erro: Preço não pode ser menor ou igual a zero.")
                return
            estoque[nome]['preco'] = novo_preco
        if nova_qtd_str:
            estoque[nome]['quantidade'] = int(nova_qtd_str)

        print(f"{nome} atualizado.")

    except ValueError:
        print("Erro: O valor digitado não é um número válido.")

# Função para excluir produto do estoque
# A função remove um produto do estoque, com confirmação antes de apagar
def excluir_produto():
    nome = input("Qual produto será retirado do estoque? ").strip().capitalize()
    if nome in estoque:
        # Confirmação antes de apagar
        confirma = input(f"Tem certeza que quer apagar '{nome}'? (s - Confirma) (n - Cancela): ").lower()
        if confirma == 's':
            del estoque[nome]
            print(f"'{nome}' foi removido.")
        else:
            print("Operação cancelada.")
    else:
        print("Produto não encontrado.")

def visualizar_estoque():
    if not estoque:
        print("\nO estoque está vazio.")
        return

    # O comando "="*30" é usado para criar uma linha de separação visual 

    print("\n" + "="*30)
    print("      ESTOQUE ATUAL")
    print("="*30)
    for nome, dados in estoque.items():
        
        print(f"-> {nome}")
        print(f"   Preço: R$ {dados['preco']:.2f} | Qtd: {dados['quantidade']}")
        print("-"*30)

#Exibir o menu de opções
while True:
    print("\n[1] Adicionar Produto no estoque\n[2] Atualizar Produto no estoque\n[3] Excluir Produto do estoque\n[4] Ver Estoque\n[5] Sair do estoque")
    escolha = input("\nO que deseja fazer? > ")

    if escolha == '1':
        adicionar_produto()
    elif escolha == '2':
        atualizar_produto()
    elif escolha == '3':
        excluir_produto()
    elif escolha == '4':
        visualizar_estoque()
    elif escolha == '5':
        print("Até mais!")
        break
    else:
        print("Opção inválida, tente de novo.")