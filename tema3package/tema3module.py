# suma tuturor numerelor de la 0 la n
def sum_of_numbers(n):
    if n <= 0:
        return 0
    return n + sum_of_numbers(n - 1)


# suma numerelor pare de la 0 la n
def sum_of_even_numbers(n):
    if n <= 0:
        return 0
    if n % 2 == 0:
        return n + sum_of_even_numbers(n - 2)

    return sum_of_even_numbers(n - 1)


# suma numerelor impare de la 0 la n
def sum_of_odd_numbers(n):
    if n <= 0:
        return 0
    if n % 2 == 1:
        return n + sum_of_odd_numbers(n - 2)

    return sum_of_odd_numbers(n - 1)
