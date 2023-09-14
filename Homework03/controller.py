from game import Game
import ui_console
import utils


class Controller:
    """Игровой контроллер.

    Атрибуты:

        my_game -- запущенная игра."""

    def create_game(self):
        """Запуск игрового контроллера."""
        ui_console.clear()

        ans = input('Кто будет ходить первым, X или O?')
        if not (ans == 'X' or ans == 'O'):
            return print("Ошибка! Запустите игру ещё раз и выберите одно из двух возможных значений: 'X' или 'O'!")

        # создаём игру, лимит ходов равный кол-ву ячеек и возможные комбинации для победы
        self.my_game = Game(ans)
        self.limit = len(self.my_game.field)
        self.combo = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                      [0, 3, 6], [1, 4, 7], [2, 5, 8],
                      [0, 4, 8], [2, 4, 6]]

        # здесь в будущем можно присоеденить код под другие UI
        # сейчас если UI это консоль - запускаемся с неё:
        self.play_in_console()

    def play_in_console(self):
        """Здесь мозг игры для консоли."""
        # игра начинается, поддержим будущий цикл повторами
        self.set_status_console(True)

        # заносим всё в цикл для постоянной работы в консоли
        while self.console_status:
            ui_console.clear()

            # показываем пример и поле в консоли
            ui_console.show_game(self.my_game.get_field())

            ans = input(
                f'Игрок [{self.my_game.get_move()}] введите номер поля: ')
            if ans == "":
                return print('Вы отправили пустое значение, тем самым прервали игру.')
            if utils.contains_char_in_digits(ans):
                continue

            # скорректируем ответ под ячейки которые начинаются с 0
            ans = int(ans) - 1
            if self.is_cell_valid(ans) and self.is_cell_empty(ans):
                self.my_game.fill_cell(ans)
                self.my_game.change_player()
                self.limit -= 1

                # игра окончена, можно глушить цикл и подводить итоги
                if self.limit == 0:
                    self.set_status_console(False)
                    ui_console.clear()
                    field = self.my_game.get_field()
                    ui_console.show_end(field)
                    self.game_result(field)

    # в идеале нужно каждый ход проверять на наличие 3 соединений(комбо),
    # чтобы следующие 3 соединения не пересекались,
    # но в этой игре трудно сделать "дабл килл",
    # поэтому обойдёмся простым алгоритмом
    def game_result(self, field):
        """Подытожить игру."""
        xxx = 0
        ooo = 0

        # посчитаем комбинации игроков
        for combo_id in self.combo:
            str_concat = ''
            for cell_id in combo_id:
                str_concat += field[cell_id]

            if str_concat == 'XXX':
                xxx += 1
            elif str_concat == 'OOO':
                ooo += 1

        # сравним очки комбинаций
        if xxx > ooo:
            print('\nПобедил игрок [X]!')
        elif xxx < ooo:
            print('\nПобедил игрок [O]!')
        else:
            print('\nПобедила ничья =)')

    def is_cell_valid(self, cell_id):
        """Проверка ячейки на валидность(её существование на поле).

        Ключевые аргументы:

            cell_id -- номер ячейки."""
        if -1 < cell_id < 9:
            return True
        else:
            return False

    def is_cell_empty(self, cell_id):
        """Проверка ячейки на пустоту в ней.

        Ключевые аргументы:

            cell_id -- номер ячейки."""
        if self.my_game.get_field()[cell_id] == ' ':
            return True
        else:
            return False

    def set_status_console(self, status):
        """Установка состояния работы цикла в консоли.

        Аргументы:

            status -- ставим 'True' если поддерживаем цикл или 'False' если глушим его."""
        self.console_status = status
