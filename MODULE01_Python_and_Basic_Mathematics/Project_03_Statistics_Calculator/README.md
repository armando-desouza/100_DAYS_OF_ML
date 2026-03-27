<h1 align="center">
  📊 Projeto 03: Calculadora de Estatística Descritiva
</h1>

## 🎯 Objetivo do projeto

<p align="justify">
  Desenvolver uma aplicação de terminal capaz de receber um conjunto de dados numéricos e processá-los, em tempo real, as suas principais métricas da estatística descritiva. Este projeto focar no desenvolvimento de algoritmos matemáticos fundamentais sem o uso de bibliotecas externas (como Pandas ou NumPy), fortalecendo a lógica em programação e a minha compreensão dos dados de forma mais realista.
</p>

## ✨ Funcionalidades

* **Processamento de Entradas:** Recebe uma string contínua de números, converte-os utilizando a técnica de <i>List Comprehension</i> para <code>float</code> e trata possíveis erros de digitação do utilizador (Programação Defensiva).
* **Cálculo de Tendência Central:** Determina a Média, a Mediana e a Moda dos dados inseridos.
* **Classificação de Moda Dinâmica:** O algoritmo identifica automaticamente se o conjunto de dados é Amodal, Unimodal, Bimodal ou Multimodal.
* **Métricas de Dispersão:** Identifica os valores Mínimo e Máximo, calculando a Amplitude do conjunto de dados.

## ✖️📐 Lógica Matemática Aplicada

<p align="justify">
  Para construir a análise descritiva, as seguintes fórmulas e lógicas foram implementadas via código:
</p>

* **Média (Média Aritmética):** Calculada somando todos os valores e dividindo pelo número de elementos.

  $$\mu = \frac{1}{n}\sum_{i=1}^{n}x_i$$

* **Mediana:** É o valor central de um conjunto de dados ordenado. Se o número de elementos ($n$) for ímpar, é o termo central. Se for par, é a média aritmética dos dois termos centrais:

  $$\text{Mediana} = \frac{x_{(n/2)} + x_{(n/2)+1}}{2}$$

<!-- * **Moda:** É o valor que apresenta a maior frequência absoluta no conjunto de dados. O algoritmo mapeia essas frequências através de dicionários (Hash Maps) e extrai o(s) valor(es) de pico. -->

* **Moda:** Em conjuntos de dados não agrupados, a moda não deriva de uma equação aritmética tradicional, mas sim de uma operação lógica de maximização. Matematicamente, procuramos o argumento $x$ que maximiza a função de frequência $f(x)$:
  $$Mo = \arg\max_{x} f(x)$$

* **Amplitude:** Representa a diferença entre o maior e o menor valor do conjunto, dando uma noção básica da dispersão dos dados.

  $$R = x_{max} - x_{min}$$

## 🛠️ Como executar

<p align="justify">
  1. Certifique-se de que tem o Python instalado na sua máquina.<br>
  2. No terminal, navegue até à pasta onde o ficheiro se encontra e execute o comando abaixo:
</p>

```bash
    python main.py
```

<p align="justify">
    3. Digite a sua lista de números separados por espaço (ex: <code>10 15.5 20 20 30</code>) e prima Enter.
</p>

## ✨ O que aprendi e como isso se aplica à IA?

<p align="justify">
    A Estatística Descritiva é uma das pedras angulares da Ciência de Dados, Machine Learning e Inteligência Artificial. Antes mesmo de treinar qualquer modelo preditivo, o profissional precisará realizar a <b>Análise Exploratória de Dados (EDA)</b> com a finalidade de entender a distribuição da informação. Saber programar e interpretar métricas como Média, Moda e Mediana é crucial para identificar novos <i>outliers</i> (valores atípicos), que podem enviesar ou destruir a precisão de um algoritmo de Inteligência Artificial.
</p>