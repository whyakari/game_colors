import os
import random
from time import sleep

default_color = "\033[m"
purple = "\033[1;35m"
rgb_color = "254;228;208"
color = f"\033[1;38;2;{rgb_color}m"

red = "\033[1;31m"
green = "\033[1;32m"
light = "\033[1;37m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
magenta = "\033[1;35m"
cyan = "\033[1;36m"


def arts_2d_pt_br():

    banner_by = f"""
    {color}GitHub - Banner por Moe-hacker 💙
    """

    HOPPOU = """
    \033[1;38;2;88;88;88m\033[{                   ▅▅▀▀▀▀▀▀▀▀▀▀▀▀▅
    \033[{                ▅▅▀▀▀               ▀▀▅▅
    \033[{         ▅▅▅▀▀            ▅           ▀▅
    \033[{          ▅▀      ▅▀█▅▅▀▀▅▀▅        ▅▅  ▀▅
    \033[{         ▅▀   █▅▀▀  ▀     ▀ ▀▀▅▅    █ ▀▀▅ █
    \033[{        ▅▀   ▅▀  ▅▀      ▀▅    ▀▅   █▅███▀█
    \033[{      ▅▅█▀▅ █ ▅▅▀          ▀▀   █   ████   █
    \033[{          █ █ ▅▅▅▅▅        ▅▅▅▅▅ █  ▀█▀    █
    \033[{          █ █▀ ▅▅▅ ▀      ▀ ▅▅▅ ▀█   █     █
    \033[{          █ █ █\033[40;31m█▀█\033[0m\033[1;38;2;88;88;88m█        █\033[40;31m█▀█\033[0m\033[1;38;2;88;88;88m█ █   █     █
    \033[{         █  █ █\033[31m███\033[1;38;2;88;88;88m█        █\033[31m███\033[1;38;2;88;88;88m█ █   █     ▀▅
    \033[{        ▅▀  █  ▀▀▀          ▀▀▀  █   █      █
    \033[{      ▅▀▅▀ █                     █   █      █
    \033[{     █   █ ▀▅ ▅▀▅   ▅▀▅   ▅▅     █   █      ▀▅
    \033[{    ▅█▅▅██▅ ▅██  ▀███ ▅████ ▀▅█▀▅▀   █       ▀▅
    \033[{    ███████ ▀██████████████████▀▀             █
    \033[{     █    ▀▅  ██▀ ▀██▀▀██▀▀██
    \033[{     ▀▅     ▀▀█              ▅▀     █          █
    \033[{       ▀▅    █               █     ██        ▅▀
    \033[{         ▀▅▅▅▀                ▀▀▀▀▀ █        █
    \033[{            ▀                       ▀        ▀
    """

    print(banner_by)
    print(HOPPOU)
    print_welcome_message_custom()


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def generate_color(rgb):
    return f"\033[1;38;2;{rgb}m"


def print_colored_text(color_code, text):
    print(f"{color_code}{text}\033[0m")


def generate_all_colors():
    for r in range(0, 256):
        for g in range(0, 256):
            for b in range(0, 256):
                rgb = f"{r};{g};{b}"
                color_code = generate_color(rgb)
                print_colored_text(color_code, "Texto colorido")


def print_welcome_message():
    print(f"{blue}*** CORES JOGO ***{default_color}\n")
    print("Bem-vindo ao Color Game! Nesse jogo, você ganha apostando!")
    print("A cor escolhida pela maquina. E você ira contra ele")
    print("As cores disponiveis sao as seguintes:\n")
    print(" - {0}Yellow{1}\n - {0}Blue{1}\n - {0}Green{1}\n - {0}Red{1}\n - {0}Purple{1}\n".format(yellow, default_color))


def print_welcome_message_custom():
    print(f"{blue}*** CORES JOGO ***{default_color}\n")
    print("Bem-vindo ao Cores Jogo! Em neste jogo, você ganha apostando!")
    print("As cores escolhida pela maquina. E voce ira contra ele.")
    print()


def print_initial_balance(balance):
    print(f"\n{yellow}Seu saldo inicial é R$ {balance:.2f}.{default_color}\n")


def check_balance(updated_balance):
    print_initial_balance(updated_balance)


def print_last_played_colors(played_colors):
    print(f"\n{yellow}Ultima cor jogada:{default_color}")
    for color in reversed(played_colors):
        print(f" - {color}")
    print("")


def play_round(balance):
    options = [("Yellow", 3), ("Blue", 5), ("Green", 10), ("Red", 20), ("Purple", 50)]

    chosen_color = random.choice([option[0] for option in options])

    print(f"\n{green}Seu saldo deve ser maior que R$ 1.00. Quanto você deseja apostar?{default_color}")

    while True:

        try:
            bet = float(input(f"⟩ R$ {yellow}"))
            if bet < 1.0:
                raise ValueError
            elif bet > balance:
                raise ValueError(f"Saldo insuficiente. Seu saldo é R$ {balance:.2f}.")
            break

        except ValueError as error:
            print(f"\n{red}ERRO: {error} Por favor, tente novamente.{default_color}")

    print(f"\n{yellow}Escolha uma dessas cores:{default_color}")

    for option in options:
        print(f" - {option[0]} (paga {option[1]}x)")

    while True:
        chosen_option = input("> ").strip().capitalize()
        if chosen_option not in [option[0] for option in options]:
            print(f"\n{red}Opção inválida. Por favor, tente novamente.{default_color}")
        else:
            break

    if chosen_option == chosen_color:
        payout = bet * options[[option[0] for option in options].index(chosen_option)][1]
        balance += payout
        print(f"\n{green}Parabéns! Você ganhou R$ {payout:.2f}.{default_color}")

    else:
        balance -= bet
        print(f"\n{red}Desculpe, você perdeu. A cor sorteada era {chosen_color}.{default_color}")
    return balance


def play_game():
    clear_console()
    print_welcome_message()
    balance = 100.0

    print_initial_balance(balance)

    while True:
        balance = play_round(balance)
        if balance <= 0:
            print(f"\n{red}Você perdeu todo o seu dinheiro! Fim de jogo.{default_color}")
            break
        else:
            keep_playing = input(f"\n\n{green}Você quer continuar jogando? [S/N]{default_color} ").strip().upper()

            if keep_playing != "S":
                print(f"\n{red}Fim desse jogo! Obrigado por jogar!{default_color}")
                break

    print(f"\n{yellow}Seu saldo final é R$ {balance:.2f}.{default_color}")


def menu():
    print(f"""{color}1. Iniciar Jogo 
2. Verificar Saldo 
3. Menu do Jogo
4. Sair""")


def lang_onlys():
    languages_disponibles = ["pt_br", "en_us"]
    return languages_disponibles


def change_language():
    print(f"""{green}Menu de Configurações

{yellow}1. Trocar Linguagem 
2. Voltar
""")

    prompt = str(input(f"{default_color}⟩ "))
    return prompt

def exit_game():
    print(f"\n{red}Saindo do jogo. Adeus!{default_color}")
    from sys import exit
    exit(0)

def main_menu():
    balance = 100

    while True:
        clear_console()
        arts_2d_pt_br()
        menu()

        choice = input(f"\nconsole {yellow}")

        if choice == "1":
            clear_console()
            print_welcome_message()
            balance = play_round(balance)
            input()

        elif choice == "2":
            check_balance(balance)
            input()

        elif choice == "3":
            clear_console()

            opt = change_language()

            if opt == "1":
                print("Função: sete a sua linguagem abaixo :p")

                global set_lang

                set_lang = str(input(f"{default_color}Linguagem ⟩ "))

                if set_lang == "pt_br":
                    print(f"{yellow}Você já definiu esta linguagem como padrão. Tem certeza que escolheu a correta?")
                    input()

                elif set_lang == "en_us":
                    print("ok")
                    input()

                    from languages import en_us
                    en_us.arts_2d_en_us()

                elif set_lang != lang_onlys():
                    input(f"\n{default_color}Linguagem {color}{set_lang} {red}não disponivel {default_color}ou foi digitada incorretamente. Para saber quais linguagens estão disponiveis, veja abaixo:\n\n{yellow}——⟩ {cyan}{lang_onlys()}")

            # back to menu
            elif opt == "2":
                menu()

        elif choice == "4":
            exit_game()
        else:
            print(f"\n{red}Opção inválida. Por favor, tente novamente.{default_color}")
            sleep(1)
            input()

main_menu()
