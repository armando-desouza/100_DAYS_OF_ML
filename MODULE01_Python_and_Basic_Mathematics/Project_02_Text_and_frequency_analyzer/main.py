def analisar_texto(texto):
    total_caracteres = len(texto)
    texto_limpo = texto.lower()
    pontuacoes = ".,!?;:\"'()[]"

    for p in pontuacoes:
        texto_limpo = texto_limpo.replace(p, "")

    palavras = texto_limpo.split()
    total_palavras = len(palavras)

    frequencia = {}
    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1

    palavras_ordenadas = sorted(frequencia.items(), key=lambda x: x[1], reverse=True)
    top_3 = palavras_ordenadas[:3]

    print("\n-=[=]=- Resultados da Análise -=[=]=-\n")
    print(f"Total de caracteres: {total_caracteres}")
    print(f"Total de palavras: {total_palavras}")
    print("Top 3 palavras mais frequentes: ")
    
    for palavra, contagem in top_3:
        print(f" - '{palavra}': {contagem} vezes")
    print("-" * 29 + "\n")

if __name__ == "__main__":
    print("-=[=]=-=[=]=- Analisador de Texto e Frequência -=[=]=-=[=]=-\n")

    while True:
        entrada = input("Digite um parágrafo (ou 'sair' para encerrar): ").strip()

        if entrada.lower() == 'sair':
            print("Encerrando o analisador. Até mais!")
            break

        if not entrada:
            print("O texto não pode estar vazio. Tente novamente.\n")
            continue

        analisar_texto(entrada)
