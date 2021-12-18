from functools import reduce


def find_min(num):
    min_ = num[0]
    for elem in num:
        if elem < min_:
            min_ = elem
    return min_


def find_max(num):
    max_ = num[0]
    for elem in num:
        if elem > max_:
            max_ = elem
    return max_


def find_sum(num):
    return reduce(lambda x, y: x + y, num)


def find_mul(num):
    return reduce(lambda x, y: x * y, num)


def get_file(file_name):
    with open(file_name, 'r') as file:
        data = tuple(map(int, file.read().strip().split()))
    return data


def main(file_name):
    nums = get_file(file_name)
    if len(nums) != 0:
        return find_min(nums), find_max(nums), find_sum(nums), find_mul(nums)


if __name__ == '__main__':
    try:
        main('test_data.txt')
    except OverflowError:
        print('Main function has given too large result')
