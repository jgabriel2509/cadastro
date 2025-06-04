def cadastrar_nome(cadastro):
       novo_nome = input("Digite o nome da pessoa: ")
       cadastro.append(novo_nome)
       print(f"Usuario {novo_nome} foi adicionado!") 

def listar_nomes(cadastro):
    print("\nlista de nomes cadastrado: ")
    for i, nome in enumerate(cadastro, start=1):
        print(f"{i}. {nome}")   

def excluir_nome(cadastro):
        excluir_nome = input("Digite o nome para excluir: ")
        if excluir_nome in cadastro:
            cadastro.remove(excluir_nome)
            print(f"{excluir_nome} foi removido.")
        else:
                print("Nome não encontrado.")
       
def menu():
    cadastro = []
    while True:
        print("\n--------------------SISTEMA DE CADASTRO---------------------")
        print("[1] Cadastrar nome")
        print("[2] Listar nomes")
        print("[3] Excluir nome")
        print("[0] sair")
        opcao = input("escolha uma opção: ")

        if opcao == '1':
            cadastrar_nome(cadastro)
        elif opcao == '2':
            listar_nomes(cadastro)
        elif opcao == '3':
            excluir_nome(cadastro)
        elif opcao == '0':
            print("saindo...")
            break
        else:
            print("!!! Opção invalida. Tente novamente. !!!")

menu()
