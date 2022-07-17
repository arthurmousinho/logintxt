
def limpa():
    import os
    os.system('cls')


def menu():
    print('''
                LOGIN COM ARQUIVOS TXT
            ------------------------------
                    [1] CRIAR CONTA
                    [2] FAZER LOGIN
                    [3] EXCLUIR CONTA
                    
    ''')


def nova_conta(usuario,senha):
    limpa()
    file = open(f'{usuario}.txt' , 'w')
    file.write(f"{usuario}")
    file.write(f"\n{senha}")
    file.close()
    print("Conta criada com sucesso!")     


def verificar_existencia(files):
    try:
        a = open(f"{files}.txt" , 'rt')
        a.close()
    except(FileNotFoundError):
        return True
    else:
        return False

def verificar_senha_usuario(usuario,senha):
    try:
       arquivo = open(f"{usuario}.txt" , 'r')
    except(FileNotFoundError):
        return False
    else:
        arquivo.readline()
        senha_certa = arquivo.readline()
        if senha == senha_certa:
            arquivo.close()
            return True
        else:
            arquivo.close()
            return False
