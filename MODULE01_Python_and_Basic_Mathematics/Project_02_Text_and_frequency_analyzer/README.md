<h1 align="center">
  📝 Projeto 02: Analisador de Texto e Frequência
</h1>

## Objetivo do projeto

<p align="justify">
  Desenvolver um script em Python capaz de receber um parágrafo de texto e extrair estatísticas cruciais: o número total de caracteres, o total de palavras e o Top 3 das palavras mais frequentes. O foco é praticar a manipulação de strings e o uso de estruturas de dados, como dicionários, para contagem e análise.
</p>

## Funcionalidades

* **Normalização de Texto:** Converte todo o texto para minúsculas e remove pontuações indesejadas, garantindo uma contagem precisa (ex: "Olá!" e "olá" são contabilizados como a mesma palavra).
* **Tokenização Básica:** Separa o texto em palavras individuais utilizando a função nativa <code>.split()</code>.
* **Mapeamento de Frequência:** Utiliza um dicionário para armazenar e atualizar a contagem de cada palavra em tempo real.
* **Ordenação Inteligente:** Aplica funções <code>lambda</code> para ordenar os dados e extrair o Top 3 de forma eficiente.
* **Loop Interativo:** O programa mantém-se em execução, permitindo analisar múltiplos textos até que o utilizador digite <code>sair</code>.

## Como executar

<p align="justify">
    1. Certifique-se de que tem o Python instalado na sua máquina.<br>
    2. No terminal, navegue até à pasta onde o ficheiro se encontra e execute o comando abaixo:
</p>

```bash
    python nome_do_seu_arquivo.py
```

<p align="justify">
    3. Digite ou cole o parágrafo de texto que deseja analisar e prima Enter para ver os resultados.
</p>

## O que aprendi e como isso se aplica à IA?

<p align="justify">
    Este projeto representa um dos meus primeiros passos práticos no <b>Processamento de Linguagem Natural (NLP)</b>. Nesse projeto foi visto um processo muito interressante, antes de um modelo de Inteligência Artificial conseguir interpretar texto, os dados precisam serem limpos (como a remoção de pontuação que implementei) e divididos em unidades menores chamadas <i>tokens</i>. A lógica de contagem de frequência de palavras desenvolvida aqui é o princípio exato por trás dos algoritmos clássicos de Machine Learning, como o <i>Bag of Words (BoW)</i> e o <i>TF-IDF</i>, que são a base para sistemas de análise de sentimentos e classificação de documentos.
</p>