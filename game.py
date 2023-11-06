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

def arts_2d():

    banner_by = f"""
    {color}GitHub - Banner By Moe-hacker 💙
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
    print(f"{blue}*** COLOR GAME ***{default_color}\n")
    print("Welcome to the Color Game! In this game, you must guess")
    print("the color chosen by the computer. Each round, you can place")
    print("a bet and choose one of the following colors:\n")
    print(" - {0}Yellow{1}\n - {0}Blue{1}\n - {0}Green{1}\n - {0}Red{1}\n - {0}Purple{1}\n".format(yellow, default_color))


def print_welcome_message_custom():
    print(f"{blue}*** COLOR GAME ***{default_color}\n")
    print("Welcome to the Color Game! In this game, you must guess")
    print("the color chosen by the computer. Each round, you can place")
    print()


def print_initial_balance(balance):
    print(f"\n{yellow}Your initial balance is R$ {balance:.2f}.{default_color}\n")


def check_balance(updated_balance):
    print_initial_balance(updated_balance)


def print_last_played_colors(played_colors):
    print(f"\n{yellow}Last played colors:{default_color}")
    for color in reversed(played_colors):
        print(f" - {color}")
    print("")


def play_round(balance):
    options = [("Yellow", 3), ("Blue", 5), ("Green", 10), ("Red", 20), ("Purple", 50)]

    chosen_color = random.choice([option[0] for option in options])

    print(f"\n{green}Your minimum bet is R$ 1.00. How much do you want to bet?{default_color}")

    while True:
        try:
            bet = float(input(f"> R$ {yellow}"))
            if bet < 1.0:
                raise ValueError
            elif bet > balance:
                raise ValueError(f"Insufficient balance. Your balance is R$ {balance:.2f}.")
            break

        except ValueError as error:
            print(f"\n{red}ERROR: {error} Please try again.{default_color}")

    print(f"\n{yellow}Choose one of the following options:{default_color}")

    for option in options:
        print(f" - {option[0]} (pays {option[1]}x)")

    while True:
        chosen_option = input("> ").strip().capitalize()
        if chosen_option not in [option[0] for option in options]:
            print(f"\n{red}Invalid option. Please try again.{default_color}")
        else:
            break

    if chosen_option == chosen_color:
        payout = bet * options[[option[0] for option in options].index(chosen_option)][1]
        balance += payout
        print(f"\n{green}Congratulations! You won R$ {payout:.2f}.{default_color}")

    else:
        balance -= bet
        print(f"\n{red}Sorry, you lost. The chosen color was {chosen_color}.{default_color}")
    return balance


def play_game():
    clear_console()
    print_welcome_message()
    balance = 100.0

    print_initial_balance(balance)

    while True:
        balance = play_round(balance)
        if balance <= 0:
            print(f"\n{red}You lost all your money! Game Over.{default_color}")
            break
        else:
            keep_playing = input(f"\n\n{green}Do you want to continue playing? [S/N]{default_color} ").strip().upper()

            if keep_playing != "S":
                print(f"\n{red}End of the game! Thanks for playing!{default_color}")
                break

    print(f"\n{yellow}Your final balance is R$ {balance:.2f}.{default_color}")


def menu():
    print(f"""{color}1. Play Game 
2. Check Balance
3. Menu Game
4. Exit""")


def change_language():
    print(f"""{green}Menu Settings

{yellow}1. Change Your Language 
2. Back
""")

    prompt = str(input(f"{default_color}⟩ "))
    return prompt


def exit_game():
    print(f"\n{red}Exiting the game. Goodbye!{default_color}")
    from sys import exit
    exit(0)


def lang_onlys():
    languages_disponibles = ["pt_br", "en_us"]
    return languages_disponibles


def main_menu():
    balance = 100

    while True:
        clear_console()
        arts_2d()
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
                print("Function: Set Your Language")

                global set_lang

                set_lang = str(input(f"{default_color}Language ⟩ "))

                if set_lang == "pt_br":
                    print("ok")
                    input()

                    from languages import pt_br
                    pt_br.arts_2d_pt_br()

                elif set_lang == "en_us":
                    print("ok")
                    input()

                    from languages import en_us
                    en_us.arts_2d_en_us()

                elif set_lang != lang_onlys():
                    input(f"\n{default_color}Language {color}{set_lang} {red}not disponible {default_color}or was type incorrect. For about of which languages has disponibles, lock it:\n\n{yellow}——⟩ {cyan}{lang_onlys()}")

            # back to menu
            elif opt == "2":
                menu()

        elif choice == "4":
            exit_game()
        else:
            print(f"\n{red}Invalid choice. Please try again.{default_color}")
            sleep(1)
            input()

main_menu()
