# !/usr/bin/env python3

# Includere modul pentru tema 3
from tema3package.tema3module import *


def main():
    print(f'Resultat testare sum_numbers(): {test_sum_numbers()} ')
    n = read_number()
    print(f'Numarul introdus este:     {n}')
    print(f'Suma numerelor de la 0 la 10:        {sum_of_numbers(10)}')
    print(f'Suma numerelor pare de la 0 la 10:   {sum_of_even_numbers(10)}')
    print(f'Suma numerelor impare de la 0 la 10: {sum_of_odd_numbers(10)}')


# Citirea unui numar intreg de la tastatura
def read_number():
    try:
        n = int(input("Introduceti un nr. intreg: "))
        return n
    except ValueError as e:
        return 0


# Testare functie de insumare a numerelor intregi si reale
def test_sum_numbers():
    if sum_numbers() == 0:
        if sum_numbers(2, 4, 'abc', param1=2) == 6:
            return sum_numbers(1, 5, 1.1, -3, 'abc', [12, 56, 'cad']) == 4.1

    return False


# Insumarea numerelor intregi si reale
def sum_numbers(*args, **kwargs):
    sum = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            sum += arg

    return sum


if __name__ == '__main__':
    main()
