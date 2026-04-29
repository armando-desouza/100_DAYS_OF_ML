<h1
    align="center"
>
    Projeto 08: Comprovador da Lei dos Grandes Números 🎲🪙
</h1>

## 📝 Descrição

Este projeto é um simulador interativo desenvolvido em Python que comprova na prática a **Lei dos Grandes Números**. O programa permite que o usuário simule milhares (ou até milhões) de lançamentos de uma moeda ou de um dado de 6 faces, calculando a probabilidade empírica e demonstrando como a aleatoriedade converge para a probabilidade teórica conforme o volume de dados aumenta.

## 🔄 Fluxograma de Navegação

O programa foi construído com um menu em loop contínuo, tratamento de erros e limpeza de tela, seguindo esta estrutura lógica:

```flowchart
    A[Início] --> B[Limpar Tela e Mostrar Menu]
    B --> C{Escolha do Usuário?}
    C -->|Opção 1| D[Simulação: Moeda]
    C -->|Opção 2| E[Simulação: Dado de 6 Faces]
    C -->|Opção 0| F[Encerrar Programa]
    C -->|Inválida| G[Mensagem de Erro]
    D --> H[Aguardar 'Enter']
    E --> H
    G --> H
    H --> B
```