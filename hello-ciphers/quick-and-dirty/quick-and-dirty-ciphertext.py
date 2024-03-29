import string


def init_ciphermap(key_list, value_list):
    """
    Initialise a dictionary with the desired mapping.
    :param key_list: the list of keys to define
    :param value_list: the list of values to which to map the keys
    :return: a dictionary with the desired mapping
    """
    return dict(zip(key_list, value_list))


def print_alphabetic_ciphertext(ciphertext, ciphermap):
    """
    Print an alphabetic version of the given ciphertext to the console.
    :param ciphertext: the ciphertext list which should be iterated over
    :param ciphermap: the dictionary to use to map the ciphertext
    :return: None
    """
    for item in ciphertext:
        if item.isnumeric():
            key = int(item) % 26
            if key in ciphermap:
                print(ciphermap[key], end='')
            else:
                print('?', end='')
        else:
            print(item, end='')


if __name__ == "__main__":
    ciphertext = [
        '9', '1', '7', '68',
        ' ',
        '51', '2', '8', '11',
        ' ',
        '7', '68',
        ' ',
        '19', '23', '8', '9', '1',
        ' ',
        '2',
        ' ',
        '9', '7', '51', '87', '18', '9',
        ' ',
        '9', '23',
        ' ',
        '2',
        ' ',
        '18', '68', '51', '2', '3', '18',
        ' ',
        '8', '23', '23', '14',
        ' ',
        '56', '2', '14', '18'
    ]

    ciphermap = init_ciphermap(list(range(0, 26)), string.ascii_lowercase)
    print_alphabetic_ciphertext(ciphertext, ciphermap)
