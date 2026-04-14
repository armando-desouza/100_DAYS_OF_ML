<h1 align="center">
    Jogo de Adivinhação Numérica 🎲
</h1>

## 🎯 Objetivo do projeto

<p
    align="justify"
>
    Este projeto é um jogo interativo de adivinhação via terminal (CLI) desenvolvido em Python. O objetivo do jogador é descobrir um número secreto gerado aleatoriamente pelo sistema entre 1 e 100. O desafio é usar a lógica e as dicas fornecidas pelo jogo para acertar o número dentro de um limite de 7 tentativas.
</p>

## ✨ Funcionalidades

* **Geração Aleatória:** Criação de um número secreto único a cada partida usando a biblioteca **random**.

* **Sistema de Dicas:** O jogo informa se o palpite do usuário foi "muito ALTO" ou "muito BAIXO", guiando os próximos passos.

* **Validação de Entrada:** Proteção contra erros de digitação (letras ou símbolos), evitando que o jogo quebre inesperadamente (``isdigit()``).

* **Histórico de Palpites:** Rastreamento e exibição de todos os números tentados ao final da partida.

* **Limpeza de Tela Dinâmica:** Interface limpa e agradável, com suporte a múltiplos sistemas operacionais (Windows, Linux e macOS) usando a biblioteca ``os``.

* **Tratamento de Exceções:** Encerramento seguro do programa caso o usuário pressione Ctrl+C ou ocorra um erro inesperado (``try...except``).


## ✖️📐 Lógica Matemática Aplicada
Desigualdades Matemáticas: A estrutura de decisão principal do jogo é baseada em desigualdades (maior que e menor que). Ao comparar o palpite com o número secreto, o código usa a lógica para segmentar os números restantes.

Probabilidade e Espaço Amostral: O jogador começa com uma probabilidade de acerto de 1%, pois o espaço amostral é de 100 números. A cada dica recebida (maior ou menor), o espaço amostral é reduzido drasticamente, o que aumenta matematicamente as chances de acerto nas tentativas seguintes se o jogador usar as dicas de forma lógica.

## 🛠️ Como executar
Certifique-se de ter o Python instalado em sua máquina.

Salve o código em um arquivo chamado main.py (ou outro nome de sua preferência).

Abra o seu terminal ou Prompt de Comando.

Navegue até a pasta onde o arquivo foi salvo.

Execute o seguinte comando:

```bash
    python main.py
```

## ✨ O que aprendi e como isso se aplica à IA?
Lógica de Busca Binária: O sistema de dicas de "maior ou menor" ensina intuitivamente o conceito do algoritmo de Busca Binária. Por exemplo, ao chutar o número 50 e receber a dica de que o alvo é "maior", eliminamos metade das possibilidades (de 1 a 50) em uma única jogada. Essa lógica de "dividir para conquistar" é essencial para a eficiência de algoritmos de busca e otimização na Ciência da Computação.

Fundamentos de Aprendizado por Reforço (Reinforcement Learning): A dinâmica deste jogo reflete de forma simplificada como as Inteligências Artificiais aprendem. O jogador atua como o "agente" que toma uma ação (um palpite). O jogo funciona como o "ambiente", que processa a ação e retorna um estado e uma recompensa/penalidade (a dica direcional e o consumo de uma tentativa). Assim como um modelo de IA ajusta seus "pesos" com base em feedback para minimizar erros, o jogador ajusta seus palpites futuros com base nas dicas recebidas para alcançar a meta final.