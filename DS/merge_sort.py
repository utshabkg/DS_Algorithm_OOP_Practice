# space complexity is not optimized.

def merge_sorted_lists(a: list, b: list):
    sorted_list = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1

        while i <len(a):
            sorted_list.append(a[i])
            i+= 1
        while j < len(b):
            sorted_list.append(b[j])
            j += 1

    return sorted_list

def merge_sort(arr: list):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[ :mid]
    right = arr[mid: ]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_sorted_lists(left, right)

if __name__ == '__main__':
    # print(merge_sorted_lists([1, 4, 6], [6, 24, 28]))
    print(merge_sort([28, 1, 6, 24, 4, 6]))