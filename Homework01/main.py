# Дан список целых чисел numbers. Необходимо написать в императивном и декларативном стилях процедуры для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_list_imperative(list):
    is_repeat = True

    while is_repeat:
        is_repeat = False
        for i in range(0, len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                is_repeat = True


def sort_list_declarative(numbers):
    return numbers.sort()


#Перейдём к тестам
my_numbers = [2, 4, 1, 3, 6, 5]

sort_list_imperative(my_numbers)
# sort_list_declarative(my_numbers)
print(my_numbers)
