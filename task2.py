def get_name_sum(name):
    sum = 0
    for letter in name:
        # 65 is ascii for 'A'
        sum += ord(letter) - 64
    return sum


def get_names_list_from_file(filename):
    names_file = open(filename, 'r', encoding='utf-8')
    names = names_file.read()
    names_file.close()

    names = names.replace("\"", "")
    names_list = names.split(',')
    return names_list


if __name__ == "__main__":
    s_names_list = sorted(get_names_list_from_file('names.txt'))

    products = []
    i = 0
    while (i < len(s_names_list)):
        products.append(get_name_sum(s_names_list[i]) * (i + 1))
        i += 1

    print(sum(products))