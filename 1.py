def concat(num: int) -> str:
    """Определение падежа от подаваемого значения."""
    if num % 100 in (11, 12, 13, 14) or num % 10 in (5, 6, 7, 8, 9, 0):
        return str(num) + ' компьютеров'
    elif num % 10 in (2, 3, 4):
        return str(num) + ' компьютера'
    else:
        return str(num) + ' компьютер'


if __name__ == '__main__':
    number = int(input())
    result = concat(number)
    print(result)

