# по умолчанию класс родитель наследуется от object
# для такого класса не обязательно вписывать object
class Game(object):
    """Подготовить партию в классические крестики-нолики.

    Ключевые аргументы:

        whose_move -- кто первым ходит (по умолчанию 'X')."""

    # по умолчанию первым будет ходить игрок 'X', либо передать аргумент букву 'O'
    def __init__(self, whose_move = 'X'):
        self.whose_move = whose_move
        self.field = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def fill_cell(self, cell_id):
        """Заполнить выбранную ячейку тем кто ходит в данный момент.

        Ключевые аргументы:

            field_id -- номер поля."""
        self.field[cell_id] = self.whose_move

    def change_player(self):
        """Сменить игрока для хода в текущей игре."""
        if self.whose_move == 'X':
            self.whose_move = 'O'
        else:
            self.whose_move = 'X'

    def get_move(self):
        """Узнать чей ход.

        Ход может быть игрока X или O."""
        return self.whose_move

    def get_field(self):
        """Получить ячейки из поля(поле целиком).

        Лист из 9 значений."""
        return self.field
