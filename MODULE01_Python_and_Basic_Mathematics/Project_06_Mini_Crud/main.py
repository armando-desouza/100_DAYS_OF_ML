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

sistema_notas = carregar_dados()
print("Sistema iniciado! Dados carregados: ", sistema_notas)