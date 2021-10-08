#Definindo as Funções:

def telaDeSelecao():
    print("Seleciona uma opção:")
    print("[1] Cadastrar Novo Usuário")
    print("[2] Listar Usuários.")
    print("[3] Listar Usuários, por ordem alfabética de acordo com o Nome de Usuário")
    print("[4] Remover Usuário")
    print("[5] Alterar Nome de Usuário.") 
    print("[6] Para encerrar o programa")

#Main do Programa
def main():
    opcaoDoPrograma = 0
    while(opcaoDoPrograma >= 0 and opcaoDoPrograma <= 5):   #Laço de Repetição Principal da função
        telaDeSelecao()

        if(opcaoDoPrograma == 1):
            print("1")
        elif(opcaoDoPrograma == 2):
            print("2")
        elif(opcaoDoPrograma == 3):
            print("3")
        elif(opcaoDoPrograma == 4):
            print("4")
        elif(opcaoDoPrograma == 5):
            print("5")
    print("-------//-Fim da Aplicação-//-------") 

if __name__ == "__main__":
    main()