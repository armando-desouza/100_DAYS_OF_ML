<h1 align="center">
  🎒 Projeto 06: Mini CRUD - Sistema de Gerenciamento de Notas
</h1>

<p align="center">
  Avançando na jornada do <b>100 Days of ML</b>! Este projeto introduz o conceito de CRUD (Create, Read, Update, Delete) e persistência de dados, habilidades vitais para qualquer manipulação e armazenamento de Datasets.
</p>

## 🎯 Objetivo do Projeto

<p align="justify">
  Desenvolver um sistema de linha de comando para gerenciar as notas de alunos. O programa permite:
</p>

  - **Adicionar novos alunos.**
  - **Listar todos os cadastros.**
  - **Buscar alunos específicos pelo seu ID de identificação.**
  - **Calcular as médias das notas.**
  - **Salvar e carregar essas informações num ficheiro de texto local.**


<p align="justify">
  O principal foco educativo aqui é dominar o uso de <code>Dicionários</code> e <code>Listas</code> aninhadas, além de aprender a manipular ficheiros de texto (<code>I/O - Input/Output</code>) em Python, garantindo que os dados não sejam perdidos quando o programa é encerrado.
</p>

## ✨ Funcionalidades

* **Persistência de Dados (I/O):** Leitura automática de um ficheiro `alunos.txt` ao iniciar e gravação dos dados ao sair, garantindo que o histórico não se perde.
* **Sistema de IDs Automáticos:** Geração inteligente de IDs únicos para cada novo aluno cadastrado.
* **Operações de CRUD:**
  * **Create:** Adição de novos alunos e suas respectivas 3 notas.
  * **Read:** Visualização de todos os alunos cadastrados ou busca filtrada por ID.
  * **Update/Processing:** Cálculo dinâmico da média aritmética das notas de cada aluno.
* **Interface Dinâmica e Colorida:** Uso da biblioteca `colorama` e limpeza de terminal (`os.system`) para proporcionar uma navegação limpa, com menus claros e feedback visual intuitivo.
* **Tratamento de Exceções:** * `FileNotFoundError`: O programa não quebra se o ficheiro `alunos.txt` ainda não existir na primeira execução.
  * `ValueError`: Impede o travamento do sistema caso o utilizador digite letras onde são esperados IDs ou notas numéricas.

## 🛠️ Como Executar

1. Certifique-se de que tem o Python instalado na sua máquina.

```bash
    python --version
```

2. Este projeto utiliza a biblioteca externa de cores. Instale-a executando no terminal:

```bash
    pip install colorama
```

3. Em seguida, navegue até a pasta onde o projeto está salvo e execute o script principal:

```bash
    python main.py
```

<p
    align="justify"
>
    Nota: O ficheiro alunos.txt será criado automaticamente na mesma pasta assim que você fechar o programa pela primeira vez escolhendo a opção "0. Sair e Salvar".
</p>

## 🧠 O que aprendi e como isso se aplica à IA?

<p align="justify">
  Em Machine Learning e Inteligência Artificial, o primeiro passo de qualquer projeto é a ingestão de dados. A lógica que utilizamos neste Mini CRUD para ler e salvar as informações no ficheiro <code>alunos.txt</code>, manipulando textos com o método <code>.split()</code>, é o princípio exato por trás do processamento e carregamento de <i>Datasets</i>. Na prática, as IAs dependem de rotinas robustas de <i>Input/Output</i> (I/O) para conseguir extrair conhecimentos de grandes ficheiros (como CSVs ou JSONs), permitindo que os modelos matemáticos sejam treinados com dados reais preservados no disco.
</p>

<p align="justify">
  Além disso, o uso de Dicionários para estruturar os dados em memória, utilizando o ID do aluno como chave de busca (<i>key</i>), introduz o conceito fundamental de indexação de dados. No futuro, ao utilizar bibliotecas profissionais de Data Science como o Pandas, a manipulação de grandes volumes de informação exigirá essa mesma compreensão lógica. Saber organizar e buscar dados específicos rapidamente através de chaves únicas é o que garante a eficiência, a escalabilidade e a velocidade na preparação das informações antes de as entregarmos a um algoritmo de IA.
</p>