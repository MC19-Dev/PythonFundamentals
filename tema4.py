import requests
import re
from bs4 import BeautifulSoup


def main():
    URL = 'https://frsah.ro/loturi'
    soup = parse_URL(URL)

    while True:
        title = input('Titlu jucatori: ').strip()
        filename = input('Nume fisier: ').lower().strip()

        write_names(get_names(soup, title), filename)

        choice = input(
            'Doriti sa afisati continutul fisierului in consola?[d/n]').lower()[0]
        if choice == 'd':
            print_names(filename)

        choice = input('Doriti sa preluati alti jucatori? ').lower()[0]
        if choice != 'd':
            break


# Print to the console the names
def print_names(filename):
    with open(filename, 'r') as file:
        names = file.readlines()
        for name in names:
            print(name, end='')


# Write the players'names in the text file
def write_names(names, filename):
    with open(filename, 'w') as file:
        for name in names:
            file.write(name + '\n')


# Get the names of players depending on the title
def get_names(soup, title):
    str_pattern = '^'+ title + '$'
    p_titles = soup.find_all('p', string=re.compile(str_pattern, flags=re.I))

    names = list()
    for p_title in p_titles:
        div_title = p_title.find_parent('div')
        super_div_title = div_title.parent.parent
        h2_name = super_div_title.find('h2')
        name = h2_name.text.strip()
        names.append(name)

    return names


# Parse the URL
def parse_URL(url):
    page = requests.get(url)
    return BeautifulSoup(page.content, 'html.parser')


if __name__ == '__main__':
    main()
