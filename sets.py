# Eliminar los repetidos de una lista con sets

def remove_duplicates(some_list):
    return list(set(some_list))


def run():
    my_list = [1, 1, 2, 3, 4, 56, 56, 23, 12]
    print(remove_duplicates(my_list))
    print(type(remove_duplicates(my_list)))


if __name__ == '__main__':
    run()
