def find_divisors(nums: list) -> list:
    """Определение общих делителей в списке произвольной длины."""

    min_num = min(nums)
    divisors = set()

    for i in range(2, min_num + 1):
        if min_num % i == 0:
            divisors.add(i)

    for num in nums:
        divisors = divisors.intersection(set(i for i in range(2, num + 1) if num % i == 0))

    return list(divisors)


if __name__ == '__main__':
    test_case = [int(x) for x in input().split()]
    result = find_divisors(test_case)
    print(result)
