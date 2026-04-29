from random import *
from os import *

def limpar_tela():
    system('cls' if name == 'nt' else 'clear')

def main():
    while True:
        limpar_tela()
        print("\n =-+-=-+-=- COMPROVADOR DE PROBABILIDADE DA LEI DOS GRANDES NÚMEROS -=-+-=-+-=\n")
        print("1. Moeda (Cara ou Coroa).")
        print("2. Dado de 6 Faces.")
        print("0. Sair.")

        escolha = input("Escolha a simulação (1 ou 2): ")
        if escolha == '1':
            cara_ou_coroa()
        elif escolha == '2':
            dado_de_6_faces()
        elif escolha == '0':
            print("\nSaindo do simulador. Até a próxima!\n")
            break
        else:
            print("\nOpção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")
        

def cara_ou_coroa():
    print("\n =-+-=-+-=- SIMULADOR DE MOEDA -=-+-=-+-=\n")

    try:
        num_lancamentos = int(input("Digite o número de lançamentos: "))
        total_caras = 0

        for i in range(num_lancamentos):
            resultado = choice(['Cara', 'Coroa'])

            if resultado == 'Cara':
                total_caras += 1

        probabilidade = total_caras / num_lancamentos
        print(f"\nA probabilidade de dar CARA em {num_lancamentos} lançamentos foi de {probabilidade:.2%}.")
    except ValueError:
        print("\n[ERRO] Você deve digitar um número inteiro válido!")

    input("\nPressione Enter para voltar ao menu principal...")

def dado_de_6_faces():
    print("\n =-+-=-+-=- SIMULADOR DE DADO -=-+-=-+-=\n")
    try:
        num_lancamentos = int(input("Digite o número de lançamentos: "))
        lado_escolhido = int(input("Qual face do dados você escolhe? (1, 2, 3, 4, 5 ou 6)"))
        total_acertos = 0

        for i in range (num_lancamentos):
            lado_aleatorio = choice([1, 2, 3, 4, 5, 6])

            if lado_aleatorio == lado_escolhido:
                total_acertos += 1
        
        probabilidade = total_acertos / num_lancamentos
        print(f"\nA probabilidade de o lado sorteado ser {lado_escolhido} em {num_lancamentos} lançamentos foi de {probabilidade:.2%}.")

    except ValueError:
        print("\n[ERRO] Você deve digitar números inteiros válidos!")

    input("\nPressione Enter para voltar ao menu principal...")

if __name__ == "__main__":
    main()
