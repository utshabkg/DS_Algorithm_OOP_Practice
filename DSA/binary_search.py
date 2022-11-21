def binary_search(list: list, number_to_find: int):
    left_index = 0
    right_index = len(list) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2

        if list[mid_index] == number_to_find:
            return list[mid_index], mid_index

        elif list[mid_index] < number_to_find:
            left_index = mid_index + 1

        elif list[mid_index] == number_to_find:
            right_index = mid_index - 1

def binary_search_recursion(list: list, number_to_find: int, left_index: int, right_index: int):
    if right_index < left_index:
        return -1, -1

    mid_index = (left_index + right_index) // 2
    if mid_index < 0 or mid_index >= len(list):
        print("Number not in the list.")
        return -1, -1

    if list[mid_index] == number_to_find:
        return list[mid_index], mid_index

    elif list[mid_index] < number_to_find:
        left_index = mid_index + 1

    elif list[mid_index] == number_to_find:
        right_index = mid_index - 1

    binary_search_recursion(list, number_to_find, left_index, right_index)

if __name__ == '__main__':
    l = [12, 15, 18, 21, 24]

    number, index = binary_search(l, 18)
    print("With Loop:", number, "is in the index",index)

    number, index = binary_search_recursion(l, 180, 0, len(l)-1)
    print("With Recursion:", number, "is in the index", index)
