def factorial(n):
    res = 1
    i = 2
    while i <= n:
        res *= i
        i += 1
    return res


def get_zeroes(n):
    f = factorial(n)
    f_str_rev = str(f)[::-1]
    f_rev_int = int(f_str_rev)
    return len(f_str_rev) - len(str(f_rev_int))


if __name__ == "__main__":
    # print(get_zeroes(5))
    # print(get_zeroes(12))
    
    n = int(input('enter a number:'))
    print(get_zeroes(n))