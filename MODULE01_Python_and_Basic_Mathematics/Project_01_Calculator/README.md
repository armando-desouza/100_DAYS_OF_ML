<h1
    align="center"
>
  🧮 Projeto 01: Calculadora Interativa de Terminal
</h1>

<p
    align="center"
>
  O primeiro passo na jornada do <b>100 Days of ML</b>. Um projeto focado em solidificar os fundamentos da linguagem Python, essenciais para a construção de lógicas e algoritmos no futuro.
</p>

## 🎯 Objetivo do Projeto

<p
    align="justify"
>
    Desenvolver uma calculadora via linha de comando que receba números e operações matemáticas básicas, mantendo-se em execução até que o utilizador decida sair.
</p>

<p
    align="justify"
>
    Mais do que fazer contas, o objetivo real deste projeto é treinar a criação de <code>funções modulares</code>, <code>tratamento de exceções</code> e <code>controle de fluxo</code> — os mesmos princípios lógicos usados para dar ferramentas ("tools") a Agentes de IA.
</p>

## ✨ Funcionalidades

* **Operações Modulares:** Funções independentes para Adição, Subtração, Multiplicação, Divisão e Exponenciação.
* **Interface Colorida:** Uso da biblioteca `colorama` para fornecer feedback visual ao utilizador (ex: mensagens de erro a vermelho, instruções a verde).
* **Tratamento de Erros Robusto:** * Prevenção contra divisão por zero.
  * Captura de erros de tipagem (`ValueError`) caso o utilizador insira texto em vez de números.
  * Validação de operações matemáticas inexistentes.
* **Loop Contínuo:** O programa mantém-se ativo num `while True` até que o comando `sair` seja invocado.

## 🛠️ Como Executar

1. Certifique-se de que tem o Python instalado na sua máquina.
2. Instale a dependência de cores executando no terminal:

```bash
    pip install colorama
```

3. Execute o script principal:

```bash
    python nome_do_seu_arquivo.py
```

## 🧠 O que aprendi e como isso se aplica à IA?

<p
    align="justify"
>
    Em Machine Learning e IA, a robustez do código é fundamental. O uso de blocos <code>try/except</code> implementados nesta calculadora é a mesma lógica utilizada para evitar que pipelines de dados quebrem quando encontram valores nulos ou inesperados num Dataset. Além disso, estruturar cada operação matemática como uma função separada é o primeiro passo para entender como arquitetar Actions para LLMs (Large Language Models).
</p>