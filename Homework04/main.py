from numpy import corrcoef as corr_pirson
from random import randint as rand_int


def get_corr(arr1: list[int], arr2: list[int]) -> float:
    return corr_pirson(arr1, arr2)[0, 1]


if __name__ == '__main__':
    array1 = [rand_int(0, 9) for _ in range(10)]
    array2 = [rand_int(0, 9) for _ in range(10)]

    print(array1)
    print(array2)
    print(f'Корреляция Пирсона между массивами: {get_corr(array1, array2)}')
