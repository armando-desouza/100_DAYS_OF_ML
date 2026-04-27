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

def transpor_matriz(matriz):
    resultado = []
    linhas_transposta = len(matriz[0])
    colunas_transposta = len(matriz)

    for i in range(linhas_transposta):
        nova_linha = []
        for j in range(colunas_transposta):
            nova_linha.append(matriz[j][i])
        resultado.append(nova_linha)

    return resultado

def somar_matrizes(matriz_a, matriz_b):
    resultado = []
    for i in range(len(matriz_a)):
        nova_linha = []
        for j in range(len(matriz_b[0])):
            nova_linha.append(matriz_a[i][j] + matriz_b[i][j])
        resultado.append(nova_linha)

def multiplicar_escalar(matriz, escalar):
    resultado = []
    for linha in matriz:
        nova_linha = []
        for elemento in linha:
            nova_linha.append(elemento * escalar)
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
            matriz_resultado = multiplicar_escalar(matriz_a, escalar)
            imprimir_matriz(matriz_resultado)
        elif opcao == '2':
            print("\n-&--&--&--&- Adição de Matrizes -&--&--&--&-")
            matriz_a = ler_matriz("Matriz A")
            matriz_b = ler_matriz("Matriz B")
        elif opcao == '3':
            print("\n-&--&--&--&- Transposição de Matrizes -&--&--&--&-")
            matriz_a = ler_matriz("Matriz A")
            matriz_resultado = transpor_matriz(matriz_a)
            imprimir_matriz(matriz_resultado)

            if len(matriz_a) == len(matriz_b) and len(matriz_a[0]) == len(matriz_b[0]):
                matriz_resultado = somar_matrizes(matriz_a, matriz_b)
                imprimir_matriz(matriz_resultado)
            else:
                print("Erro: As matrizes precisam ter exatamente o mesmo tamanho para a adição!")

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
