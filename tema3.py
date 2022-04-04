def main():
    print(sum_numbers('1', 2.3, 'a', 1, 3, 7, a='5', i='vesta'))


def sum_numbers(*args, **kwargs):
    sum = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            sum += arg

    return sum

if __name__ == '__main__':
    main()


