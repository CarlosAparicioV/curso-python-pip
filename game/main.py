import random


def choose_options():
    options = ("piedra", "papel", "tijera")
    # Player chooses option
    user_option = input("¿Piedra, papel o tijera? -> ")
    user_option = user_option.lower()
    if not user_option in options:  # User's option validation
        print("Esa opción no es válida")
        # continue
        return None, None

    # Computer chooses option
    computer_option = random.choice(options)

    # Comunicate both choices
    print("User option ->", user_option)
    print("Computer option ->", computer_option)

    return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print("¡EMPATE!")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("Piedra gana a tijera")
            print("¡GANASTE!")
            user_wins += 1
        else:
            print("Papel gana a piedra")
            print("¡TÚ PIERDES!")
            computer_wins += 1
    elif user_option == "papel":
        if computer_option == "piedra":
            print("Papel gana a piedra")
            print("¡GANASTE!")
            user_wins += 1
        else:
            print("Tijera gana a papel")
            print("¡TÚ PIERDES!")
            computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("Tijera gana a papel")
            print("¡GANASTE!")
            user_wins += 1
        else:
            print("Piedra gana a tijera")
            print("¡TÚ PIERDES!")
            computer_wins += 1
    return user_wins, computer_wins


def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1
    while True:
        print("*" * 10)
        print("ROUND", rounds)
        print("*" * 10)
        print("computer wins:", computer_wins)
        print("user wins:", user_wins)

        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(
            user_option, computer_option, user_wins, computer_wins)
        if check_winner(user_wins, computer_wins) == False:
            break
        rounds += 1


def check_winner(user_wins, computer_wins):
    if computer_wins == 3:
        print("El rotundo ganador es la computadora")
        return False
    if user_wins == 3:
        print("¡Eres el ganador absoluto!")
        return False


run_game()
