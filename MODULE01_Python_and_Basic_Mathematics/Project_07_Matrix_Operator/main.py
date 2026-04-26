def ler_matriz(nome_matriz):
    print(f"\n-&--&--&--&- Criando a {nome_matriz} -&--&--&--&-")
    qtd_linhas = int(input("Quantas linhas? "))
    qtd_colunas = int(input("Quantas colunas? "))

    matriz_final = []

    for i in range(qtd_linhas):
        linha_atual = []

        for j in range(qtd_colunas):
            numero = float(input(f"Digite o número da posição [linha {i+1}, coluna {j+1}]: "))
            linha_atual.append(numero)

        matriz_final.append(linha_atual)

    return matriz_final

def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)
    
    print("-&-" * 15)

def multiplicar_escalr(matriz, escalar):
    resultado = []

    for linha in matriz:
        nova_linha = []

        resultado.append(nova_linha)
    
    return resultado

def main():
    while True:
        print("\n-&--&--&--&- 🧮 CALCULADORA DE MATRIZES -&--&--&--&-")
        print("1. Multiplicação por Escalar.")
        print("2. Adição de Matrizes.")
        print("3. Transposição de Matrizes.")
        print("0. Sair.")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\n-&--&--&--&- Multiplicação por Escalar -&--&--&--&-")

            matriz_a = ler_matriz("Matriz A")
            escalar = float(input("Adicione um número escalar para multiplicar a matriz: "))

            multiplicar_escalar(matriz, escalar)

        elif opcao == '0':
            print("Encerrando o programa...")
            break
        
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()

# minha_matriz = ler_matriz("Matriz A")

# print("Nossa Matriz Inicial:")
# imprimir_matriz(minha_matriz)
