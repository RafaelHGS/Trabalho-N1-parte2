'''
    Técnicas de Programação
-Atividade N1 - Parte 2

Nome:   Gabriel de Souza Alves              RA: 21587787
Nome:   Gustavo Mello Soares dos Santos     RA: 21568663
Nome:   Rafael Henrique Gonçalves Soares    RA: 21566288

'''

#Criação de Variáveis/Listas Globais
usuariosCadastrados = []
usuariosEmAlfabetico = []

#Definindo as Funções:

def telaDeSelecao():
    print("Seleciona uma opção:")
    print("[1] Cadastrar Novo Usuário")
    print("[2] Listar Usuários.")
    print("[3] Buscar Usuários por Nome")
    print("[4] Remover Usuário")
    print("[5] Alterar Nome de Usuário.") 
    print("[6] Para encerrar o programa")

def cadastrandoNovoUsuario():   #Definindo Função: H1.: Como gestor do sistema gostaria de cadastrar novos usuários pelo seu nome completo e e-mail.
    cadastroDeUsuario = {}
    cadastroDeUsuario["nome"] = input("Informe o nome do Usuario: ").title()
    cadastroDeUsuario["e-mail"] = input("Informe o e-mail do Usuário: ")
    usuariosEmAlfabetico.append('Nome do Usuário: ' + cadastroDeUsuario["nome"] + " \t///\t E-mail: " + cadastroDeUsuario["e-mail"])
    usuariosCadastrados.append(cadastroDeUsuario)
    print("Usuario cadastrado!\n")
    print("-----------------------///-----------------------\n")
    
def listandoUsuario():   # H2.: Como gestor do sistema gostaria de exibir todos os usuários cadastrados, listando-os por ordem de cadastro.
    print("Nº  //\t\tUsuário\t\t///\t\t E-mail Do Usuário\n\n")
    for numeracao,usuariosPorOrdemChegada in enumerate(usuariosCadastrados):
        print(f'{numeracao} - Nome do Usuário: {usuariosPorOrdemChegada["nome"]} \t///\t E-mail: {usuariosPorOrdemChegada["e-mail"]}')
    print("\n\n-----------------------///-----------------------\n")

def listandoUsuarioPorAlpha():   # H3.: Como gestor do sistema gostaria de exibir todos os usuários cadastros, listando-os por ordem alfabética.
    print("Nº  //\t\tUsuário\t\t///\t\t E-mail Do Usuário\n\n")
    usuarioAlfabetico = sorted(usuariosEmAlfabetico)
    for numeracao, usuarioNaOrdemAlpha in enumerate(usuarioAlfabetico):
        print(numeracao, "-", usuarioNaOrdemAlpha)
    print("\n\n-----------------------///-----------------------\n")

def verificandoUsuario(nome):   #H4.: Como gestor do sistema gostaria de verificar se um usuário faz parte da lista de participantes, buscando-o pelo seu nome.
    print(f"Usuários Localizados com o nome {nome}")
    print("----//\t\tUsuário\t\t///\t\t E-mail Do Usuário\n")
    for usuario in usuariosCadastrados:
        if nome == usuario["nome"]:
            print(f'Nome do Usuário: {usuario["nome"]} \t//\t E-mail: {usuario["e-mail"]}\n')

def removendoUsuario(email):   #H5.: Como gestor do sistema gostaria poder remover um usuário cadastrado, buscando-o por seu e-mail.
    for buscandoUsuario in usuariosCadastrados:
        if email == buscandoUsuario["e-mail"]:
            usuariosCadastrados.remove(buscandoUsuario)
    for buscandoUsuario in usuariosEmAlfabetico:
        string = buscandoUsuario.split(" ")
        if email == string[6]: 
            usuariosEmAlfabetico.remove(buscandoUsuario)
            print(f'---------O Usuário de Email "{email}" foi removido---------')
            print("\n-----------------------///-----------------------\n")
            return
    print("\n---------// Usuário Não Encontrado !!! //---------\n")
    print("\n-----------------------///-----------------------\n")


def alterarUsuario(email):   #H6.: Como gestor do sistema gostaria de poder alterar o nome de um usuário cadastrado no sistema, buscando-o por seu e-mail.
    for localiza in usuariosCadastrados:
        if email == localiza["e-mail"]:
            novoNome = input("Digite o novo nome do Usuario: ").title()
            localiza["nome"] = novoNome
    for localiza in usuariosEmAlfabetico:
        palavraSeparada = localiza.split(" ")
        if email == palavraSeparada[6]:
            usuariosEmAlfabetico.remove(localiza)
            novoNomeDeUsuario = palavraSeparada
            novoNomeDeUsuario[3] = novoNome
            novoNomeDeUsuario = "Nome do Usuário: " + novoNomeDeUsuario[3] + " \t///\t E-mail: " + novoNomeDeUsuario[6]
            usuariosEmAlfabetico.append(novoNomeDeUsuario)
            print(f'---------O nome de usuário de Email "{email}" foi alterado para {novoNome}---------')
            print("\n-----------------------///-----------------------\n")
            return
    print("\n---------// Usuário Não Encontrado !!! //---------\n")
    print("\n-----------------------///-----------------------\n")
           
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
        
        #Seleção da opção apropriada, chamando cada função conforme o desejado 
        if(opcaoDoPrograma == 1):
            print("\n-----------------------///-----------------------\n")
            cadastrandoNovoUsuario()

        elif(opcaoDoPrograma == 2):
            listarPorOrdemOuPorAlpha = 0
            #Laço para tratamento de erros de Digitação:
            while listarPorOrdemOuPorAlpha <=0 or listarPorOrdemOuPorAlpha >=3:
                print("[1] Listagem por ordem de Cadastro")
                print("[2] Listagem por ordem Alfabética")

                try:   #Tratamento de Erros
                    listarPorOrdemOuPorAlpha = int(input())
                except:
                    print("-------//-Informe uma tarefa válida!-//-------")
                    continue
                #Seleção da função conforme o Desejado
                if listarPorOrdemOuPorAlpha == 1:
                    print("\n-----------------------///-----------------------\n")
                    listandoUsuario()
                elif listarPorOrdemOuPorAlpha == 2:
                    print("\n-----------------------///-----------------------\n")
                    listandoUsuarioPorAlpha()

        elif(opcaoDoPrograma == 3):
            print("\n-----------------------///-----------------------\n")
            verificandoUsuario(input("Informe um nome para buscar na lista: ").title())
        elif(opcaoDoPrograma == 4):
            print("\n-----------------------///-----------------------\n")
            removendoUsuario(input("Informe o e-mail do usuário a ser removido: "))
        elif(opcaoDoPrograma == 5):
            print("\n-----------------------///-----------------------\n")
            alterarUsuario(input("Informe o e-mail do usuário para alterar o seu nome: "))
        elif(opcaoDoPrograma != 6):
            print("\n-----------------------///-----------------------\n")
            print("\n-------//-Informe uma tarefa válida!-//-------\n")
            opcaoDoPrograma = 0
            continue
    print("-------//-Fim da Aplicação-//-------")         
#Início de programa
if __name__ == "__main__":
    main()
