def cadastrar_nome(cadastro):
    try:
        novo_nome = input("Digite o nome da pessoa: ").strip()
        if novo_nome:
            cadastro.append(novo_nome)
            print(f"Usuário '{novo_nome}' foi adicionado!")
        else:
            print("Nome inválido. Tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro ao cadastrar o nome: {e}")

def listar_nomes(cadastro):
    try:
        if not cadastro:
            print("\nNenhum nome cadastrado ainda.")
            return
        print("\nLista de nomes cadastrados:")
        for i, nome in enumerate(cadastro, start=1):
            print(f"{i}. {nome}")
    except Exception as e:
        print(f"Ocorreu um erro ao listar os nomes: {e}")

def excluir_nome(cadastro):
    try:
        if not cadastro:
            print("Nenhum nome para excluir.")
            return
        nome_para_excluir = input("Digite o nome para excluir: ").strip()
        if nome_para_excluir in cadastro:
            cadastro.remove(nome_para_excluir)
            print(f"'{nome_para_excluir}' foi removido.")
        else:
            print("Nome não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao excluir o nome: {e}")

def menu():
    cadastro = []
    while True:
        try:
            print("\n-------------------- SISTEMA DE CADASTRO ---------------------")
            print("[1] Cadastrar nome")
            print("[2] Listar nomes")
            print("[3] Excluir nome")
            print("[0] Sair")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == '1':
                cadastrar_nome(cadastro)
            elif opcao == '2':
                listar_nomes(cadastro)
            elif opcao == '3':
                excluir_nome(cadastro)
            elif opcao == '0':
                print("Saindo...")
                break
            else:
                print("!!! Opção inválida. Tente novamente. !!!")
        except Exception as e:
            print(f"Ocorreu um erro no menu: {e}")

# Inicia o programa
menu()

