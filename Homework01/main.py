# Дан список целых чисел numbers. Необходимо написать в императивном и декларативном стилях процедуры для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_list_imperative(numbers):
    isRepeat = True

    while (isRepeat):
        isRepeat = False
        for i in range(0, len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                temp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = temp
                isRepeat = True


def sort_list_declarative(numbers):
    return numbers.sort()


#Перейдём к тестам
my_numbers = [2, 4, 1, 3, 6, 5]

sort_list_imperative(my_numbers)
# sort_list_declarative(my_numbers)
print(my_numbers)
