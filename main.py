import defs

while True:
    defs.menu()

    try:
        opcao = int(input("> "))
    except(ValueError,TypeError):
        print("Tente novamente")
    else:
        if opcao > 3 or opcao < 1:
            print("Opção inválida, tente novamente: ")

        elif opcao == 1:  # opção de criar conta 
            try:
                defs.limpa()
                usuario = str(input("Novo usuário: "))
                senha = str(input("Nova senha: "))

                if not defs.verificar_existencia(usuario): 
                    print("Usuário já exixtente, tente novamente")
                    continue
            except(ValueError,TypeError):
                defs.limpa()
                print("Tente novamente")
            else:
                defs.nova_conta(usuario,senha)

        elif opcao == 2: #opção de fazer login
            try:
                defs.limpa()
                usuario_login = str(input("Usuário: "))
                senha_login = str(input("Senha [números]: "))  
            except(ValueError,TypeError):
                defs.limpa()
                print("Tente novamente")
            else:
                if not defs.verificar_senha_usuario(usuario_login,senha_login):
                    defs.limpa()
                    print("Erro no login tente novamente")
                else:
                    defs.limpa()
                    print(f"BEM VINDO, {usuario_login}")
        elif opcao == 3: # opção excluir conta
            try:
                defs.limpa()
                usuario_login = str(input("Usuário: "))
                senha_login = str(input("Senha [números]: "))  
            except(ValueError,TypeError):
                defs.limpa()
                print("Tente novamente")
            else:
                if not defs.verificar_senha_usuario(usuario_login,senha_login):
                    defs.limpa()
                    print("Erro no login tente novamente")
                else:
                    defs.limpa()
                    print("Conta excluída com sucesso !!")
                    import os
                    os.remove(f"{usuario_login}.txt")
