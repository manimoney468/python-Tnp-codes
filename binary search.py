def binary_search_first_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            result = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result


def binary_search_last_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            result = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result


in_arr = [1, 2, 2, 2, 3, 4, 5]
in_arr.sort()
print(in_arr)

target = 2

first_occurrence = binary_search_first_occurrence(in_arr, target)
last_occurrence = binary_search_last_occurrence(in_arr, target)

if first_occurrence != -1:
    print("First occurrence of", target, "is at index", first_occurrence)
else:
    print("Element", target, "not found in the array.")

if last_occurrence != -1:
    print("Last occurrence of", target, "is at index", last_occurrence)
else:
    print("Element", target, "not found in the array.")

binary_search(in_arr_mid_second, mid, h)
