import random
import string
from colorama import init, Fore, Style

init(autoreset=True)

def generate_password(length):
    if length < 8:
        return "Erro: O tamanho mínimo da senha deve ser 8 para ser considerada minimamente segura."
    
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_characters = uppercase_letters + lowercase_letters + digits + symbols
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    random.shuffle(password)

    return "".join(password)

def validate_password(password):
    if len(password) < 8:
        return "Fraca: A senha deve ter pelo menos 8 caracteres."
    
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    if has_uppercase and has_lowercase and has_number and has_symbol:
        return "Forte: Excelete! Sua senha é muito segura." 
    else:
        missing_elements = []
        if not has_uppercase: missing_elements.append("letra maiúscula")
        if not has_lowercase: missing_elements.append("letra minúscula")
        if not has_number: missing_elements.append("número")
        if not has_symbol: missing_elements.append("símbolo")

        return f"Fraca: Faltam os seguintes elementos -> {', '.join(missing_elements)}."
    

if __name__ == "__main__":
    print(Fore.CYAN + Style.BRIGHT + "\n===8==8==8==8=== GERADOR E VALIDADOR DE SENHAS ===8==8==8==8===\n")
    print(Fore.CYAN + "Bem-vindo! Digite 'sair'  a qualquer momento para encerrar.\n")

    while True:
        print(Fore.RED + Style.BRIGHT + "\n" + "===8==8==8===" * 5 + "\n")

        try:
            user_input = input(Fore.YELLOW + "Digite o TAMANHO da senha, 'validar' ou 'sair': ").strip().lower()
            
            if user_input == 'sair':
                print(Fore.MAGENTA + Style.BRIGHT + "Encerrando o programa. Até logo!\n")
                break

            elif user_input == 'validar':
                user_password = input(Fore.YELLOW + "Digite a senha que deseja validar: ")
                validation_password = validate_password(user_password)
                
                if "Forte" in validation_password:
                    print(Fore.GREEN + Style.BRIGHT + f"Resultado: {validation_password}")
                else:
                    print(Fore.RED + Style.BRIGHT + f"Resultado: {validation_password}")
            
            else:
                desired_length = int(user_input)
                new_password = generate_password(desired_length)

                if "Erro" in new_password:
                    print(Fore.RED + Style.BRIGHT + new_password)

                else:
                    print(Fore.GREEN + f"\nSua senha gerada: {new_password}\n")
                    
                    validation_password = validate_password(new_password)
                    if "Forte" in validation_password:
                        print(Fore.GREEN + Style.BRIGHT + f"Validação automática: {validate_password(new_password)}")
                    else: 
                        print(Fore.RED + Style.BRIGHT + f"Validação automática: {validate_password(new_password)}")
        except ValueError:
            print("Entrada inválida! Por favor, digite um valor válido, ('validar' ou 'sair').")
        
        except (KeyboardInterrupt, EOFError):
            print("\nPrograma interrompido forçadamente pelo usuário. Até mais!")
            break
