from random import *
from os import *

def limpar_tela():
    system('cls' if name == 'nt' else 'clear')

def jogo_adivinhacao():
    limpar_tela()

    while True:
        numero_secreto = randint(1, 100)
        limite_tentativas = 7
        tentativas_usadas = 0
        historico = []

        print("\n" + "=~" * 30 + "\n")
        print(" Bem-vindo ao Jogo de Adivinhação Numérica! \n")
        print("\n" + "=~" * 30 + "\n")
        print(f"Eu pensei em um número entre 1 e 100.")
        print(f"Você tem um {limite_tentativas} tentativas para adivinhar.\n")

        while tentativas_usadas < limite_tentativas:

            try:
                entrada = input("\n\nDigite o seu melhor palpite: ")
            except KeyboardInterrupt:
                print("\n\nVocê interrompeu o jogo (Ctrl + C). Até a próxima!")
                return
            except EOFError:
                print("\n\nFim de entrada detectado. Até a próxima!")
                return
            except Exception as e:
                print(f"\n\nErro inesperado: {e}. Encerrando o jogo...")
                return
            
            
            if entrada == 'sair':
                print("\nVocê decidiu sair do jogo. Até a próxima")
                return
            
            if not entrada.isdigit():
                print("Por favor, digite apenas números inteiros!")
                continue

            palpite = int(entrada)
            historico.append(palpite)
            tentativas_usadas += 1

            limpar_tela()

            if palpite == numero_secreto:
                print(f"\n🎉 PARABÉNS! Você acertou o número {numero_secreto} em {tentativas_usadas} tentativa(s)!")
                break

            elif palpite < numero_secreto:
                print(f"Seu último palpite foi: {palpite}")
                print("DICA: Seu palpite foi muito BAIXO.")
                
            else:
                print(f"Seu último palpite foi: {palpite}")
                print("DICA: Seu palpite foi muito ALTO.")

            tentativas_restantes = limite_tentativas - tentativas_usadas
            
            if tentativas_restantes > 0:
                print(f"Você ainda tem {tentativas_restantes} tentativa(s) restante(s).\n")
            else:
                print(f"\n😢 Que pena! Suas tentativas acabaram. O número secreto era {numero_secreto}.")

        
            print("\n =~= RESUMO DO JOGO =~=")
            print(f"Seu histórico de palpites: {historico}")
            print("\n" + "=~" * 30 + "\n")

        try:
            jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
            if jogar_novamente != 's':
                print("\nObrigado por jogar! Encerrando o programa...")
                break

        except KeyboardInterrupt:
            print("\n\nFim de entrada detectado. Saindo com segurança. Até mais!")
            break

        except EOFError:
            print("\n\nFim de entrada detectado. Saindo com segurança. Até mais!")
            break

        except Exception as e:
            print("\n\nUm erro inesperado aconteceu: {e}. Encerrando...")
            break

if __name__ == "__main__":
    jogo_adivinhacao()