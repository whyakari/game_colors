import os
import random
from time import sleep

# Definition of colors
default_color = "\033[m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
purple = "\033[1;35m"

rgb_color = "254;228;208"
color = f"\033[1;38;2;{rgb_color}m"


def arts_2d():
    LINE = int((int(os.popen('stty size', 'r').read().split()[1])) / 2 - 24)
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

    print(HOPPOU)
    print_welcome_message_custom()


# Function to clear the console
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


# Function to print the welcome message
def print_welcome_message():
    print(f"{blue}*** COLOR GAME ***{default_color}\n")
    print("Welcome to the Color Game! In this game, you must guess")
    print("the color chosen by the computer. Each round, you can place")
    print("a bet and choose one of the following colors:\n")
    print(" - {0}Yellow{1}\n - {0}Blue{1}\n - {0}Green{1}\n - {0}Red{1}\n - {0}Purple{1}\n".format(yellow, default_color))


# Message custom of the welcome
def print_welcome_message_custom():
    print(f"{blue}*** COLOR GAME ***{default_color}\n")
    print("Welcome to the Color Game! In this game, you must guess")
    print("the color chosen by the computer. Each round, you can place")
    print()

# Function to print the initial balance
def print_initial_balance(balance):
    print(f"\n{yellow}Your initial balance is R$ {balance:.2f}.{default_color}\n")


# Função para consultar o saldo total
def check_balance(updated_balance):
    print_initial_balance(updated_balance)


# Function to print the last played colors
def print_last_played_colors(played_colors):
    print(f"\n{yellow}Last played colors:{default_color}")
    for color in reversed(played_colors):
        print(f" - {color}")
    print("")


# Function to play a round of the game
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


# Function to play the game
def play_game():
    clear_console()
    print_welcome_message()
    balance = 100.0

    # balance initial
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

    # Exibe o saldo final
    print(f"\n{yellow}Your final balance is R$ {balance:.2f}.{default_color}")


# Função do menu principal
def main_menu():
    balance = 100
    while True:
        clear_console()
        arts_2d()
        print(f"{color}")
        print("1. Play Game")
        print("2. Check Balance")
        print("3. Exit")

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
            print(f"\n{red}Exiting the game. Goodbye!{default_color}")
            break
        else:
            print(f"\n{red}Invalid choice. Please try again.{default_color}")
            sleep(1)
            input()


# main code execute
main_menu()

