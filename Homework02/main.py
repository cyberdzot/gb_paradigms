# На вход подается число n.
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.

# Код написан в 2 парадигмах, 'структурной' и 'процедурной'
# структурная - используется for и не используется goto( по другому если придумать наверное спагетти какое то получится =) ) 
# процедурная - код обёрнут в метод/функцию по другому процедура собственно
# код полезно обворачивать в метод/функцию для дальнейшей удобной подачи в другие какие то приложения


def func(n):
    for i in range(1, n):
        print(f"1 * {i} = {1 * i}")


# пусть будет до 4
func(4)
