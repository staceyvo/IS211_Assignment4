import datetime
import random


def insertion_sort(sort_list):
    """This function, insertion_sort will sort a list.

                        Args:
                            sort_list holds a list of random numbers

                        Returns:
                            Returns an ordered list.

                """
    for index in range(len(sort_list)):
        for left in range(index):
            if sort_list[index] < sort_list[left]:
                current = sort_list[index]
                sort_list[index] = sort_list[left]
                sort_list[left] = current




def shell_sort(sort_list):
    """This function, shell_sort will sort a list.

                        Args:
                            sort_list holds a list of random numbers

                        Returns:
                            Returns an ordered list.

                """
    gap = len(sort_list) / 2
    #creates multiple passes through list
    while gap > 0:
        index = 0
        #scan from left to right minus our gap
        while index + gap < len(sort_list):
            if sort_list[index + gap] < sort_list[index]:
                current = sort_list[index + gap]
                sort_list[index + gap] = sort_list[index]
                sort_list[index] = current

                #scans from right to left plus our gap
                right_index = index
                while right_index - gap > 0 and sort_list[right_index] < sort_list[right_index - gap]:
                    current = sort_list[right_index - gap]
                    sort_list[right_index - gap] = sort_list[right_index]
                    sort_list[right_index] = current
                    right_index - gap

            index += 1
        gap /= 2



def python_sort(sort_list):
    sort_list.sort()


if __name__ == '__main__':


    # ins_sort = [random.randint(0, 100) for _ in range(25)]
    # print(ins_sort)
    # start = datetime.datetime.now()
    # insertion_sort(ins_sort)
    # duration = datetime.datetime.now() - start
    # print(ins_sort)
    # print(duration)
    # print('')



    for func in [insertion_sort, shell_sort, python_sort]:
        small = [random.randint(0, 1e7) for _ in range(500)]
        medium = [random.randint(0, 1e7) for _ in range(1000)]
        large = [random.randint(0, 1e7) for _ in range(10000)]
        for sort_list in [small, medium, large]:
            start = datetime.datetime.now()
            func(sort_list)
            duration = datetime.datetime.now() - start
            print('{}: {}'.format(func.__name__, duration))
        print('')
