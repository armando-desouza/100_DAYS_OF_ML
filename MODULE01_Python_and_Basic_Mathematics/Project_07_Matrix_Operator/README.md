<h1 align="center">
  🧮 Projeto 07: Calculadora de Matrizes
</h1>

<p align="center">
  Avançando na jornada do <b>100 Days of ML</b>! Este projeto introduz os fundamentos da Álgebra Linear através de código puro, uma habilidade essencial para compreender como os algoritmos de Inteligência Artificial processam dados matematicamente.
</p>

## 🎯 Objetivo do Projeto

<p align="justify">
  Desenvolver um sistema interativo de linha de comando para criar e realizar operações matemáticas complexas com matrizes (tabelas de números). O programa permite:
</p>

  - **Construir matrizes dinâmicas definindo linhas e colunas.**
  - **Realizar a Multiplicação por um número Escalar.**
  - **Fazer a Adição de Matrizes de tamanhos iguais.**
  - **Realizar a Transposição de Matrizes (inverter linhas e colunas).**

<p align="justify">
  O principal foco educativo aqui é dominar a lógica de programação por trás das estruturas de dados bidimensionais, utilizando <code>Listas de Listas</code> e múltiplos <code>Loops Aninhados (for)</code> para navegar e manipular os índices (i, j) matematicamente, sem depender de bibliotecas externas prontas.
</p>

## ✨ Funcionalidades

* **Geração Dinâmica de Dados:** Função dedicada para o utilizador construir matrizes personalizadas digitando elemento por elemento.
* **Menu Interativo (Loop de Navegação):** Utilização de `while True` e estruturas condicionais para manter o programa rodando até o utilizador decidir sair.
* **Operações Matemáticas Puras:**
  * **Multiplicação Escalar:** Iteração sobre cada elemento da matriz para aplicar a operação matemática e retornar uma nova tabela.
  * **Adição Protegida:** Verificação lógica prévia dos tamanhos das matrizes (usando `len()`). O cálculo só é realizado se as matrizes forem exatamente do mesmo tamanho.
  * **Transposição:** Lógica avançada de cruzamento de índices para transformar as colunas da matriz original nas linhas da nova matriz.
* **Exibição Formatada:** Função dedicada para imprimir as listas na tela simulando visualmente o formato de grade/tabela de uma matriz real.

## 🛠️ Como Executar

1. Certifique-se de que tem o Python instalado na sua máquina.

```bash
    python --version
```

2. Navegue até a pasta onde o projeto está salvo.

3. Execute o script principal no terminal:

```bash
    python main.py
```

## 🧠 O que aprendi e como isso se aplica à IA?

<p align="justify">
  Neste projeto, o maior aprendizado foi dominar a manipulação de estruturas de dados bidimensionais através de listas de listas e múltiplos loops aninhados. Ao construir algoritmos matemáticos do zero, como a transposição e a soma, desenvolvi um raciocínio lógico sólido sobre como acessar e modificar índices específicos (i, j) dentro de uma matriz. Esse nível de controle manual sobre os dados é fundamental, pois exige entender a engenharia interna das operações em vez de apenas usar funções prontas. Compreender essa lógica estrutural passo a passo é o alicerce absoluto para qualquer processamento e organização avançada de informações no futuro.
</p>

<p align="justify">
  No universo da Inteligência Artificial, os algoritmos não processam dados soltos, mas sim agrupados em matrizes e tensores. A lógica matemática que apliquei aqui é exatamente o motor das Redes Neurais, onde cálculos de "pesos" são feitos através de operações matriciais contínuas. Na Visão Computacional, por exemplo, uma imagem é lida pela IA puramente como uma grande matriz de pixels, e comandos como a multiplicação escalar alteram esses valores diretamente. Portanto, dominar essa base estrutural na mão torna o aprendizado futuro de bibliotecas essenciais da área, como NumPy e PyTorch, muito mais claro e intuitivo.
</p>