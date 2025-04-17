field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def print_field():
    for row in field:
        print('|'.join(row))
        if row != field[-1]:
            print('-+-+')


def make_move(player_symbol):
    while True:
        try:
            x, y = input(f"Введите координаты вашего хода ({player_symbol}) через пробел (строка столбец): ").split()
            x, y = int(x), int(y)

            if not (0 <= x < 3 and 0 <= y < 3):
                raise ValueError("Координаты вне диапазона!")

            if field[x][y] != ' ':
                raise ValueError("Эта ячейка занята!.")

            field[x][y] = player_symbol
            break
        except ValueError as e:
            print(e)


def check_win(symbol):
    for i in range(3):
        if all(field[i][j] == symbol for j in range(3)): return True
        if all(field[j][i] == symbol for j in range(3)): return True

    if all(field[i][i] == symbol for i in range(3)): return True
    if all(field[i][2 - i] == symbol for i in range(3)): return True

    return False


def main_game():
    current_player = 'X'
    moves_count = 0

    while True:
        print("\nТекущее положение:")
        print_field()

        make_move(current_player)
        moves_count += 1

        if check_win(current_player):
            print_field()
            print(f"\nИгрок {current_player} победил!\n")
            break
        elif moves_count >= 9:
            print_field()
            print("\nНичья!\n")
            break

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    main_game()