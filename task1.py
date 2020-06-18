def search_pairs(array, k):
    res = []
    sorted_arr = sorted(array)

    for el in sorted_arr:
        complement = k - el
        if (complement in sorted_arr) and ((complement, el) not in res):
            res.append((el, complement))

    return res

if __name__ == "__main__":
    array = input('enter the array space-separated:').split(' ')
    
    array = list(map(int, array))
    k = int(input('enter the target number k:'))

    print(search_pairs(array, k))