import random
import datetime
from datetime import datetime as dt


def sequential_search(search_list):
    for index in range(len(search_list)):
        if search_list[index] == -1:
            return index
    return None


def ordered_sequential_search(search_list):
    for index in range(len(search_list)):
        if search_list[index] == -1:
            return index
    return None


def binary_search_iterative(search_list):
    pass


def binary_search_recursive(search_list):
    pass


if __name__ == '__main__':
    lists500 = []
    lists1000 = []
    lists10000 = []
    list_of_lists = [
        lists500,
        lists1000,
        lists10000
    ]

    for _ in range(100):
        lists500.append([random.randint(0, 1285398243) for _b in range(500)])

        lists1000.append([random.randint(0, 1285398243) for _b in range(500)])

        lists10000.append([random.randint(0, 1285398243) for _b in range(500)])

    for mega_list in list_of_lists:
        search_time = datetime.timedelta(0, 0, 0)
        for item in mega_list:
            start = dt.now()
            sequential_search(item)
            search_time += dt.now() - start

        print(
        '{}, {} from {}'.format(sequential_search.__name__, search_time.total_seconds() / float(len(mega_list)), len(mega_list)))

    list_of_functions = [
        ordered_sequential_search,
        binary_search_iterative,
        binary_search_recursive
    ]

    for mega_list in list_of_lists:
        for item in mega_list:
            item.sort()

    for func in list_of_functions:

        for mega_list in list_of_lists:
            search_time = datetime.timedelta(0,0,0)
            for item in mega_list:
                start = dt.now()
                func(item)
                search_time += dt.now() - start

            print('{}, {} from {}'.format(func.__name__, search_time.total_seconds()/float(len(mega_list)),len(mega_list)))
