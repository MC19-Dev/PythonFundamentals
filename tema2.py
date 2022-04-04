def main():
    # Afisare lista initiala
    init_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
    print(f"Lista initiala: {init_list}")

    # Afisare lista ordonata ascendent
    asc_list = list(init_list)
    asc_list.sort()
    print(f"Lista ordonata ascendent:  {asc_list}")

    # Afisare lista ordonata descendent
    desc_list = list(init_list)
    desc_list.sort(reverse=True)
    print(f"Lista ordonata descendent: {desc_list}")

    # Afisare numere pare din lista
    print(f"Numerer pare:  {desc_list[::2]}")

    # Afisare numere impare din lista
    print(f"Numere impare: {desc_list[1::2]}")

    # Afisare numerelor multipli de 3 din lista
    multiple_3_list = [number for number in init_list if number % 3 == 0]
    print(f"Multipli de 3: {multiple_3_list}")

    # Afisare lista initiala
    print(f"Lista initiala: {init_list}")

    dict = {'Numer': 'Ionescu', 'Prenume': 'Ion'}

    print(dict.get('Nume'))
    print(dict['Nume'])


if __name__ == "__main__":
    main()
