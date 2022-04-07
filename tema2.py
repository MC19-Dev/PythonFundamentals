def main():
    # Afisare lista initiala
    init_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
    print(f"Lista initiala: {init_list}")

    # Afisare lista ordonata ascendent
    asc_list = sorted(init_list)
    print(f"Lista ordonata ascendent:  {asc_list}")

    # Afisare lista ordonata descendent
    desc_list = sorted(init_list, reverse=True)
    print(f"Lista ordonata descendent: {desc_list}")

    # Afisare numere pare din lista
    print(f"Numere pare:  {asc_list[1::2]}")

    # Afisare numere impare din lista
    print(f"Numere impare: {asc_list[::2]}")

    # Afisare numerelor multipli de 3 din lista
    print(f"Multipli de 3: {asc_list[2::3]}")

    # Afisare lista initiala
    print(f"Lista initiala: {init_list}")


if __name__ == "__main__":
    main()
