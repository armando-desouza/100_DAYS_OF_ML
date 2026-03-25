from colorama import init, Fore

init(autoreset=True)

def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return f"{Fore.RED}Erro: Não é possível dividir por zero!"
    return x / y

def exponenciar(x, y):
    if x == 0 and y < 0:
        return "{Fore.RED}Erro: Zero não pode ser elevado a um expoente negativo (divisão por zero)!"
    
    return x ** y

# 2. FUNÇÃO PRINCIPAL E LOOP

def iniciar_calculadora():
    print(f"{Fore.RED}--0--0--0-- Calculadora Interativa --0--0--0--")
    print(f"{Fore.GREEN}Operações disponíveis: +, -, *, /, **")
    print(f"{Fore.GREEN}Digite 'sair' a qualquer momento para encerrar.\n")

    while True:
        operacao = input(f"{Fore.CYAN}Escolha a operação (+, -, *, /, **)").strip()

        if operacao.lower() == 'sair':
            print(f"{Fore.RED}Encerrando a calculadora. Até logo!")
            break

        if operacao not in ['+', '-', '*', '/', '**']:
            print(f"{Fore.RED}Operação inválida. Tente novamente.\n")
            continue

        num1_str = input(f"{Fore.GREEN}Digite o primeiro número: ").strip()
        if num1_str.lower() == 'sair':
            break

        num2_str = input(f"{Fore.GREEN}Digite o segundo número: ").strip()
        if num2_str.lower() == 'sair':
            break

        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
            print(f"{Fore.RED}Erro: Por favor, digite apenas números válidos.\n")
            continue

        if operacao == '+':
            resultado = adicionar(num1, num2)
        elif operacao == '-':
            resultado = subtrair(num1, num2)
        elif operacao == '*':
            resultado = multiplicar(num1, num2)
        elif operacao == '/':
            resultado = dividir(num1, num2)
        elif operacao == '**':
            resultado = exponenciar(num1, num2)

        print(f"{Fore.CYAN}Resultado: {resultado}\n")

if __name__ == "__main__":
    iniciar_calculadora()        
