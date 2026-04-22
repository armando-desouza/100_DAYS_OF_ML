def carregar_dados():
    alunos = {}

    try:
        with open('alunos.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()

            if conteudo:
                lista_de_alunos = conteudo.split('|')

                for aluno_texto in lista_de_alunos:
                    dados = aluno_texto.split(',')

                    if len(dados) == 5:
                        id_aluno = int(dados[0])
                        nome = dados[1]

                        notas = [float(notas[2]), float(dados[3]), float(dados[4])]

                        alunos[id_aluno] = {
                            'nome': nome,
                            'notas': notas
                        }
    except FileNotFoundError:
        pass

    return alunos

def exibir_menu():
    print("\n=0=0= 🎒 SISTEMA DE GERENCIAMENTO DE NOTAS =0=0=\n")
    print("1. Adicionar Aluno.")
    print("2. Exibir/Buscar Aluno.")
    print("3. Calcular Médias.")
    print("0. Sair e Salvar.")
    print("\n=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=\n")

def main():
    sistema_notas = carregar_dados()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == 1:
            print("\n[Em construção] Aqui vamos adicionar um aluno...")
        elif opcao == 2:
            print("\n[Em construção] Aqui vamos exibir/buscar alunos...")
        elif opcao == 3:
            print("\n[Em construção] Aqui vamos calcular as médias...")
        elif opcao == 0:
            print("\nEncerrando o sistema. Até logo! 👋")
        else:
            print("\n❌ Opção inválida! Por favor, digite um número de 0 a 3.") 


if __name__ == "__main__":
    main()
