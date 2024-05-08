def create_table(number: int):
    """Создание таблицы умножения."""

    default = [int(x) for x in range(1, number + 1)]

    print(' ', *default)

    for row in range(1, number + 1):
        current = [int(x) * row for x in range(1, number + 1)]
        print(row, *current)


if __name__ == '__main__':
    number = int(input())
    create_table(number)
