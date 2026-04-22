from colorama import init, Fore, Style
import os

init(autoreset=True)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

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

                        notas = [float(dados[2]), float(dados[3]), float(dados[4])]

                        alunos[id_aluno] = {
                            'nome': nome,
                            'notas': notas
                        }
    except FileNotFoundError:
        pass

    return alunos

def exibir_menu():
    print(f"\n{Fore.YELLOW}=0=0= 🎒 SISTEMA DE GERENCIAMENTO DE NOTAS =0=0=\n")
    print(f"{Fore.GREEN}1. Adicionar Aluno.")
    print(f"{Fore.GREEN}2. Exibir/Buscar Aluno.")
    print(f"{Fore.GREEN}3. Calcular Médias.")
    print(f"{Fore.GREEN}0. Sair e Salvar.")
    print(f"\n{Fore.YELLOW}=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=\n")

def main():
    sistema_notas = carregar_dados()

    while True:
        limpar_tela()
        exibir_menu()
        
        opcao = input(f"{Fore.CYAN}Escolha uma opção: ")
        if opcao == '1':
            adicionar_aluno(sistema_notas)

        elif opcao == '2':
            print("\n1. Ver todos os alunos.")
            print("2. Buscar aluno por ID.")
            sub_opcao = input("Escolha: ")

            if sub_opcao == '1':
                exibir_alunos(sistema_notas)
            elif sub_opcao == '2':
                buscar_alunos(sistema_notas)
            else:
                print("❌ Opção inválida.")

        elif opcao == '3':
            calcular_medias(sistema_notas)

        elif opcao == '0':
            salvar_dados(sistema_notas)
            break

        else:
            print(f"\n{Fore.RED}❌ Opção inválida! Por favor, digite um número de 0 a 3.") 
    

def adicionar_aluno(sistema_notas):
    print(f"\n{Fore.YELLOW} =0=0= ➕ ADICIONAR NOVO ALUNO =0=0=\n")
    nome = input("Digite o nome do aluno: ")

    try:
        nota1 = float(input("Digite a 1ª nota: "))
        nota2 = float(input("Digite a 2ª nota: "))
        nota3 = float(input("Digite a 3ª nota: "))
    except ValueError:
        print("❌ Erro: Por favor, digite apenas números para as notas (use ponto para casas decimais, ex: 9.5).")
        return
    
    if sistema_notas:
        novo_id = max(sistema_notas.keys()) + 1
    else:
        novo_id = 1

    sistema_notas[novo_id] = {
        'nome': nome,
        'notas': [
            nota1,
            nota2,
            nota3
        ]
    }

    print(f"{Fore.YELLOW}✅ Aluno '{nome}' adicionado com sucesso! (ID gerado: {novo_id}).")

def exibir_alunos(sistema_notas):
    print(f"\n{Fore.YELLOW} =0=0= 📋 LISTA DE ALUNOS =0=0=\n")

    if not sistema_notas:
        print("Nenhum aluno cadastrado ainda.")
        return
    
    for id_aluno, dados in sistema_notas.items():
        nome = dados['nome']
        notas = dados['notas']
        print(f"ID: {id_aluno} | Nome: {nome} | Notas: {notas}")

def buscar_alunos(sistema_notas):
    print(f"\n{Fore.YELLOW} =0=0= 🔍 BUSCAR ALUNOS =0=0=\n")

    if not sistema_notas: 
        print("Nenhum aluno cadastrado ainda.")
        return
    
    try:
        id_busca = int(input("Digite o ID do aluno que deseja buscar: "))
    except ValueError:
        print("❌ Erro: O ID deve ser um número inteiro.")
        return
    
    if id_busca in sistema_notas:
        aluno = sistema_notas[id_busca]
        print(f"\n ✅ Aluno encontrado!")
        print(f"ID: {id_busca} | NOME: {aluno['nome']} | NOTAS: {aluno['notas']}")
    else:
        print(f"\n ❌ Aluno com ID {id_busca} não encontrado no sistema.")

def calcular_medias(sistema_notas):
    print(f"\n{Fore.YELLOW} =0=0= 🧮 MÉDIAS DOS ALUNOS =0=0= \n")

    if not sistema_notas:
        print("Nenhum aluno cadastrado ainda.")
        return
    
    for id_aluno, dados in sistema_notas.items():
        nome = dados['nome']
        notas = dados['notas']

        media = sum(notas) / len(notas)

        print(f"ID: {id_aluno} | Nome: {nome} | Média: {media:.2f}")

def salvar_dados(sistema_notas):
    print(f"\n{Fore.YELLOW} =0=0= 🛟 SALVANDO DADOS =0=0=\n")

    with open('alunos.txt', 'w', encoding='utf-8') as arquivo:
        lista_textos_alunos = []

        for id_aluno, dados in sistema_notas.items():
            nome = dados['nome']
            notas = dados['notas']

            linha_aluno = f'{id_aluno},{nome},{notas[0]},{notas[1]},{notas[2]}'

            lista_textos_alunos.append(linha_aluno)

        texto_final = "|".join(lista_textos_alunos)
        arquivo.write(texto_final)

    print(f"{Fore.CYAN}💾 Dados salvos com sucesso no arquivo 'alunos.txt'!")

if __name__ == "__main__":
    main()

    
