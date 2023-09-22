def find_pos(num_list, number, first, last):
    if last < first:
        return None
    #
    middle = first + (last - first) // 2
    if num_list[middle] == number:
        return middle
    elif num_list[middle] < number:
        return find_pos(num_list, number, middle + 1, last)
    else:
        return find_pos(num_list, number, first, middle - 1)

FIRST_INDEX = 0
num_list = sorted([12, 1, 9, 2, 7, 3])
number = 12
print(find_pos(num_list, number, FIRST_INDEX, len(num_list) - 1))
