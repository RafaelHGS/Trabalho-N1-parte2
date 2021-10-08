#Criação de Variáveis/Listas Globais
usuariosCadastrados = []
usuariosEmAlfabetico = []

#Definindo as Funções:

def telaDeSelecao():
    print("Seleciona uma opção:")
    print("[1] Cadastrar Novo Usuário")
    print("[2] Listar Usuários.")
    print("[3] Listar Usuários, por ordem alfabética de acordo com o Nome de Usuário")
    print("[4] Remover Usuário")
    print("[5] Alterar Nome de Usuário.") 
    print("[6] Para encerrar o programa")

def cadastrandoNovoUsuario():   #Definindo Função: H1.: Como gestor do sistema gostaria de cadastrar novos usuários pelo seu nome completo e e-mail.
    cadastroDeUsuario = {}
    cadastroDeUsuario["nome"] = input("Informe o nome do Usuario: ")
    cadastroDeUsuario["e-mail"] = input("Informe o e-mail do Usuário:")
    usuariosEmAlfabetico.append('Nome do Usuário: ' + cadastroDeUsuario["nome"] + " \t///\t E-mail: " + cadastroDeUsuario["e-mail"])
    usuariosCadastrados.append(cadastroDeUsuario)
    print("Usuario cadastrado!\n")
    print("-----------------------///-----------------------\n")

def verificandoUsuario(nome):   #H4.: Como gestor do sistema gostaria de verificar se um usuário faz parte da lista de participantes, buscando-o pelo seu nome.
    print(f"Usuários Localizados com o nome {nome}")
    print("----//\t\tUsuário\t\t///\t\t E-mail Do Usuário")
    for usuario in usuariosCadastrados:
        if nome == usuario["nome"]:
            print(f'Nome do Usuário: {usuario["nome"]} \t//\t E-mail: {usuario["e-mail"]}')

#Main do Programa
def main():
    opcaoDoPrograma = 0
    while(opcaoDoPrograma >= 0 and opcaoDoPrograma <= 5):   #Laço de Repetição Principal da função
        telaDeSelecao()

        #Evitando erros de digitação no código, para se usar apenas opções válidas
        try:
            opcaoDoPrograma = int(input())  
        except:
            print("\n---------Você deve digitar um número para selecionar uma opção!!!!---------\n")
            continue

        if(opcaoDoPrograma == 1):
            print("\n-----------------------///-----------------------\n")
            cadastrandoNovoUsuario()
        elif(opcaoDoPrograma == 2):
            print("2")
        elif(opcaoDoPrograma == 3):
            print("\n-----------------------///-----------------------\n")
            verificandoUsuario(input("Informe um nome para buscar na lista: "))
        elif(opcaoDoPrograma == 4):
            print("4")
        elif(opcaoDoPrograma == 5):
            print("5")
    print("-------//-Fim da Aplicação-//-------") 

if __name__ == "__main__":
    main()