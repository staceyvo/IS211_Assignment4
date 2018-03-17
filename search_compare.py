import random
import datetime
from datetime import datetime as dt


def sequential_search(search_list, term=-1):
    for index in range(len(search_list)):
        if search_list[index] == -1:
            return index
    return None


def ordered_sequential_search(search_list, term=-1):
    for index in range(len(search_list)):
        if search_list[index] == -1:
            return index
    return None


def binary_search_iterative(search_list, elem=-1):
    left_bound = 0
    right_bound = len(search_list) - 1
    mid = (left_bound + right_bound) / 2


    while left_bound != right_bound or search_list[left_bound] == elem or search_list[right_bound] == elem:
        if elem == search_list[mid]:
            return mid
        elif elem > search_list[mid]:
            left_bound = mid + 1
        else:
            right_bound = mid
        mid = (left_bound + right_bound) / 2
    return None




def binary_search_recursive(search_list, term=-1):
    if len(search_list) == 0:
        return None

    mid = len(search_list)/2
    if search_list[mid] == term:
        return mid
    elif search_list[mid] > term:
            return binary_search_recursive(search_list[:mid], term)
    else:
        result = binary_search_recursive(search_list[mid + 1:], term)
        if result:
            return result + mid
        else:
            return result




if __name__ == '__main__':
    lists500 = []
    lists1000 = []
    lists10000 = []
    list_of_lists = [
        lists500,
        lists1000,
        lists10000
    ]
#create 100 lists for 500, 1000, 10000
    for _ in range(100):
        lists500.append([random.randint(0, 1285398243) for _b in range(500)])

        lists1000.append([random.randint(0, 1285398243) for _b in range(1000)])

        lists10000.append([random.randint(0, 1285398243) for _b in range(10000)])

    for mega_list in list_of_lists:
        search_time = datetime.timedelta(0, 0, 0)
        for item in mega_list:
            start = dt.now()
            sequential_search(item)
            search_time += dt.now() - start

        print(
        '{}, {} from {} numbers'.format(sequential_search.__name__, search_time.total_seconds() / float(len(mega_list)), len(mega_list[0])))

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

            print('{}, {} from {}'.format(func.__name__, search_time.total_seconds()/float(len(mega_list)),len(mega_list[0])))
