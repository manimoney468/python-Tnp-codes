
in_arr = [2, 3, 34, 5, 67, 8, 9]
print(in_arr)

l = 0
h = len(in_arr) - 1
mid = (l + h) // 2
print(mid)

while l <= h:
    if (in_arr[mid] > in_arr[mid + 1]) and (in_arr[mid] > in_arr[mid - 1]):
        print(mid)
        print("Success:", in_arr[mid])
        break
    elif in_arr[mid] < in_arr[mid + 1]:
        l = mid
    elif in_arr[mid - 1] > in_arr[mid]:
        h = mid
    mid = (l + h) // 2
