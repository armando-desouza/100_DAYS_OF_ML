def analisar_dados(numeros):
    quantidade = len(numeros)

    soma_total = sum(numeros)
    media = soma_total / quantidade

    numeros_ordenados = sorted(numeros)
    meio = quantidade // 2
    if quantidade % 2 == 0:
        mediana = (numeros_ordenados[meio - 1] + numeros_ordenados[meio]) / 2
    else:
        mediana = numeros_ordenados[meio]

    frequencias = {}
    for num in numeros:
        if num in frequencias:
            frequencias[num] += 1
        else:
            frequencias[num] = 1
    
    max_freq = max(frequencias.values())
    
    modas = []
    for num, freq in frequencias.items():
        if freq == max_freq:
            modas.append(num)
    
    if len(modas) == len(frequencias):
        tipo_moda = "Amodal (nenhum valor se destaca)"
        valores_moda = "Nenhum"
    elif len(modas) == 1:
        tipo_moda = "Unimodal"
        valores_moda = str(modas[0])
    elif len(modas) == 2:
        tipo_moda = "Bimodal"
        valores_moda = f"{modas[0]} e {modas[1]}"
    else:
        tipo_moda = "Multimodal"
        valores_moda = ", ".join([str(m) for m in modas])

    valor_maximo = max(numeros)
    valor_minimo = min(numeros)

    amplitude = valor_maximo - valor_minimo

    print("\n-=-=()=-=- Relatório Estatístico -=-=()=-=-\n")
    print(f"Dados analisados: {quantidade} valores")
    print(f"Média: {media:.2f}")
    print(f"Moda ({tipo_moda}): {valores_moda}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Valor Mínimo: {valor_minimo}")
    print(f"Valor Máximo: {valor_maximo}")
    print(f"Amplitude (Máx - Mín): {amplitude}")
    print("\n" + "-=-=()=-=-" * 4 + "\n")

if __name__ == "__main__":
    print("\n-=-=-=-=- Calculadora de Estatística Descritiva -=-=-=-=-\n")
    print("DICA: Digite os números separados por espaço (ex: 10 20 30.5 40)")

    while True:
        entrada = input("\nDigite os valores (ou 'sair' para encerrar): ").strip()

        if entrada.lower() == 'sair':
            print("Encerrando a calculadora. Até mais!\n")
            break
        if not entrada:
            print("Entrada vazia. Tente novamente.")
            continue

        try:
            lista_strings = entrada.split()
            lista_numeros = [float(num) for num in lista_strings]
            analisar_dados(lista_numeros)
        except ValueError:
            print("Erro: Por favor, digite apenas números válidos separados por espaço.")

    print("\n" + "-=-=-=-=" * 8 + "\n")