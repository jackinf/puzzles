import functools


def compare1(a, b):
    """ this is wrong, it fails on [824,938,1399,5607,6973,5703,9609,4398,8247] """
    for i in range(max(len(a), len(b))):
        p1 = min(len(a) - 1, i)
        p2 = min(len(b) - 1, i)
        if a[p1] == b[p2]:
            continue
        return 1 if a[p1] > b[p2] else -1
    return 0


def solve(nums):
    snums = sorted((str(num) for num in nums), key=functools.cmp_to_key(compare1), reverse=True)
    return snums


if __name__ == "__main__":
    print(solve([3,30,34,5,9]))
    # print(compare1('3', '4'))
    # print(compare1('3', '2'))
    # print(compare1('3', '3'))
    # print(compare1('3', '30'))
    # print(compare1('3', '34'))