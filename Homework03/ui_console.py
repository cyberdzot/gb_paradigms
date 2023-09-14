def clear():
    """Очистка консоли."""
    print("\033[H\033[J")


def show_game(list):
    """Монтирование консольного интерфейса во время запущенной игры."""
    print("Крестики-нолики для двоих игроков.")
    print("*Чтобы прервать игру отправьте пустое значение.")
    print("Нумерация для примера:")
    print("|1|2|3|")
    print("|4|5|6|")
    print("|7|8|9|\n")
    print("Поле для игры:")
    print(f"|{list[0]}|{list[1]}|{list[2]}|")
    print(f"|{list[3]}|{list[4]}|{list[5]}|")
    print(f"|{list[6]}|{list[7]}|{list[8]}|")


def show_end(list):
    """Монтирование консольного интерфейса во время окончания игры."""
    print("Поле для игры:")
    print(f"|{list[0]}|{list[1]}|{list[2]}|")
    print(f"|{list[3]}|{list[4]}|{list[5]}|")
    print(f"|{list[6]}|{list[7]}|{list[8]}|")


if __name__ == "__main__":
    clear()

# green = 'Зелёный'
# red = 'Красный'
# print(f"\033[32m{green}\033[0m")
# print(f"\033[31m{red}\033[0m")
