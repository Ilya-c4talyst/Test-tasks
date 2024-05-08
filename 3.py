def find_prime(left: int, right: int) -> list:
    """Поиск простых чисел в диапазоне."""
    lst = []
    for value in range(left, right + 1):
        for case in range(2, value // 2 + 1):
            if not value % case:
                break
        else:
            lst.append(value)
    return lst


if __name__ == '__main__':
    left, right = map(int, input().split())
    result = find_prime(left, right)
    print(result)
